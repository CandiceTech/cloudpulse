from app.aws.ec2_analyzer import get_idle_instances
from app.aws.s3_analyzer import analyze_s3_buckets


def get_optimization_summary():
    instances = get_idle_instances()
    buckets = analyze_s3_buckets()

    if isinstance(instances, dict) and "error" in instances:
        instances = []

    if isinstance(buckets, dict) and "error" in buckets:
        buckets = []

    monthly_ec2_savings = sum(
        item.get("potential_monthly_savings", 0) for item in instances
    )
    monthly_s3_savings = sum(
        item.get("potential_monthly_savings", 0) for item in buckets
    )
    total_monthly_savings = round(monthly_ec2_savings + monthly_s3_savings, 2)

    high_risk_items = [
        item for item in [*instances, *buckets]
        if item.get("risk_level") == "HIGH"
    ]

    return {
        "instances_analyzed": len(instances),
        "buckets_analyzed": len(buckets),
        "high_risk_resources": len(high_risk_items),
        "total_monthly_savings": total_monthly_savings,
        "total_annual_savings": round(total_monthly_savings * 12, 2),
        "recommendation": "Review high-risk resources first, then apply rightsizing and lifecycle policies."
    }
