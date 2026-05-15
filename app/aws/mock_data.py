MOCK_EC2_INSTANCES = [
    {
        "instance_id": "i-0a12cloudpulse001",
        "current_instance_type": "t3.large",
        "recommended_instance_type": "t3.medium",
        "state": "running",
        "avg_cpu": 2.4,
        "estimated_monthly_cost": 60.0,
        "optimized_monthly_cost": 30.0,
        "potential_monthly_savings": 60.0,
        "estimated_annual_savings": 720.0,
        "risk_level": "HIGH",
        "recommendation": "Potentially idle - consider stopping"
    },
    {
        "instance_id": "i-0b34cloudpulse002",
        "current_instance_type": "t3.medium",
        "recommended_instance_type": "t3.small",
        "state": "running",
        "avg_cpu": 9.8,
        "estimated_monthly_cost": 30.0,
        "optimized_monthly_cost": 15.0,
        "potential_monthly_savings": 15.0,
        "estimated_annual_savings": 180.0,
        "risk_level": "MEDIUM",
        "recommendation": "Low utilization - consider downsizing"
    },
    {
        "instance_id": "i-0c56cloudpulse003",
        "current_instance_type": "t3.micro",
        "recommended_instance_type": "t3.micro",
        "state": "running",
        "avg_cpu": 38.6,
        "estimated_monthly_cost": 8.5,
        "optimized_monthly_cost": 8.5,
        "potential_monthly_savings": 0,
        "estimated_annual_savings": 0,
        "risk_level": "LOW",
        "recommendation": "Healthy"
    }
]


MOCK_SERVICE_COSTS = {
    "Amazon Elastic Compute Cloud - Compute": 98.5,
    "Amazon Simple Storage Service": 24.75,
    "Amazon Relational Database Service": 64.2,
    "Amazon CloudWatch": 11.4
}


MOCK_S3_BUCKETS = [
    {
        "bucket_name": "cloudpulse-logs-dev",
        "estimated_storage_gb": 420,
        "estimated_monthly_cost": 9.66,
        "potential_monthly_savings": 4.83,
        "risk_level": "MEDIUM",
        "recommendation": "Move older log files to S3 Glacier Instant Retrieval"
    },
    {
        "bucket_name": "cloudpulse-backups-archive",
        "estimated_storage_gb": 1100,
        "estimated_monthly_cost": 25.3,
        "potential_monthly_savings": 18.5,
        "risk_level": "HIGH",
        "recommendation": "Apply lifecycle policy for infrequently accessed backups"
    },
    {
        "bucket_name": "cloudpulse-assets-public",
        "estimated_storage_gb": 80,
        "estimated_monthly_cost": 1.84,
        "potential_monthly_savings": 0,
        "risk_level": "LOW",
        "recommendation": "Healthy"
    }
]
