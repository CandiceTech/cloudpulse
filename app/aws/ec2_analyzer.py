import boto3
from datetime import datetime, timedelta, timezone
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

from app.aws.mock_data import MOCK_EC2_INSTANCES
from app.config import use_mock_data


# Estimated monthly EC2 pricing
INSTANCE_PRICING = {
    "t3.micro": 8.50,
    "t2.micro": 8.00,
    "t3.small": 15.00,
    "t3.medium": 30.00,
    "t3.large": 60.00
}

# Rightsizing recommendations
RIGHTSIZING_MAP = {
    "t3.large": "t3.medium",
    "t3.medium": "t3.small",
    "t3.small": "t3.micro"
}


def get_idle_instances():
    if use_mock_data():
        return MOCK_EC2_INSTANCES

    ec2 = boto3.client("ec2")
    cloudwatch = boto3.client("cloudwatch")

    try:
        response = ec2.describe_instances()
    except (BotoCoreError, ClientError, NoCredentialsError) as exc:
        return {
            "error": "Unable to read EC2 data from AWS",
            "detail": str(exc),
            "hint": "Set CLOUDPULSE_USE_MOCKS=true for local demo mode or configure AWS credentials."
        }

    idle_instances = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]

            # Skip terminated instances
            if state == "terminated":
                continue

            # Pull CloudWatch CPU metrics
            metrics = cloudwatch.get_metric_statistics(
                Namespace="AWS/EC2",
                MetricName="CPUUtilization",
                Dimensions=[
                    {
                        "Name": "InstanceId",
                        "Value": instance_id
                    }
                ],
                StartTime=datetime.now(timezone.utc) - timedelta(days=7),
                EndTime=datetime.now(timezone.utc),
                Period=86400,
                Statistics=["Average"]
            )

            datapoints = metrics["Datapoints"]

            avg_cpu = 0

            if datapoints:
                avg_cpu = sum(
                    point["Average"] for point in datapoints
                ) / len(datapoints)

            avg_cpu = round(avg_cpu, 2)

            # Current estimated monthly cost
            estimated_cost = INSTANCE_PRICING.get(instance_type, 20.00)

            # Default values
            recommendation = "Healthy"
            potential_savings = 0
            annual_savings = 0
            risk_level = "LOW"

            recommended_instance_type = instance_type
            optimized_monthly_cost = estimated_cost

            # Optimization Logic
            if avg_cpu < 5:

                recommendation = "Potentially idle - consider stopping"
                potential_savings = estimated_cost
                annual_savings = round(
                    potential_savings * 12,
                    2
                )

                risk_level = "HIGH"

                # Rightsizing suggestion
                if instance_type in RIGHTSIZING_MAP:

                    recommended_instance_type = RIGHTSIZING_MAP[
                        instance_type
                    ]

                    optimized_monthly_cost = INSTANCE_PRICING.get(
                        recommended_instance_type,
                        estimated_cost
                    )

            elif avg_cpu < 15:

                recommendation = (
                    "Low utilization - consider downsizing"
                )

                potential_savings = round(
                    estimated_cost * 0.5,
                    2
                )

                annual_savings = round(
                    potential_savings * 12,
                    2
                )

                risk_level = "MEDIUM"

                if instance_type in RIGHTSIZING_MAP:

                    recommended_instance_type = RIGHTSIZING_MAP[
                        instance_type
                    ]

                    optimized_monthly_cost = INSTANCE_PRICING.get(
                        recommended_instance_type,
                        estimated_cost
                    )

            idle_instances.append({
                "instance_id": instance_id,
                "current_instance_type": instance_type,
                "recommended_instance_type": recommended_instance_type,
                "state": state,
                "avg_cpu": avg_cpu,
                "estimated_monthly_cost": estimated_cost,
                "optimized_monthly_cost": optimized_monthly_cost,
                "potential_monthly_savings": potential_savings,
                "estimated_annual_savings": annual_savings,
                "risk_level": risk_level,
                "recommendation": recommendation
            })

    return idle_instances
