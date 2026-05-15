import boto3
from datetime import date
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

from app.aws.mock_data import MOCK_SERVICE_COSTS
from app.config import use_mock_data


# ==============================
# TOTAL MONTHLY COST
# ==============================
def get_monthly_costs():
    if use_mock_data():
        return {
            "month": date.today().replace(day=1).strftime("%B"),
            "amount": round(sum(MOCK_SERVICE_COSTS.values()), 2),
            "source": "mock"
        }

    today = date.today()
    start = today.replace(day=1)

    ce = boto3.client("ce")

    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                "Start": str(start),
                "End": str(today)
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"]
        )
    except (BotoCoreError, ClientError, NoCredentialsError) as exc:
        return {
            "error": "Unable to read cost data from AWS",
            "detail": str(exc),
            "hint": "Set CLOUDPULSE_USE_MOCKS=true for local demo mode or configure AWS credentials."
        }

    amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

    return {
        "month": start.strftime("%B"),
        "amount": round(float(amount), 2),
        "source": "aws"
    }


# ==============================
# SERVICE-BY-SERVICE COSTS
# ==============================
def get_service_costs():
    if use_mock_data():
        return MOCK_SERVICE_COSTS

    today = date.today()
    start = today.replace(day=1)

    ce = boto3.client("ce")

    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                "Start": str(start),
                "End": str(today)
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE"
                }
            ]
        )
    except (BotoCoreError, ClientError, NoCredentialsError) as exc:
        return {
            "error": "Unable to read service cost data from AWS",
            "detail": str(exc),
            "hint": "Set CLOUDPULSE_USE_MOCKS=true for local demo mode or configure AWS credentials."
        }

    results = response["ResultsByTime"][0]["Groups"]

    service_costs = {}

    for item in results:
        service_name = item["Keys"][0]
        amount = item["Metrics"]["UnblendedCost"]["Amount"]

        service_costs[service_name] = round(float(amount), 2)

    return service_costs
