import boto3
from datetime import date

# Create AWS Cost Explorer client
ce = boto3.client("ce")


# ==============================
# TOTAL MONTHLY COST
# ==============================
def get_monthly_costs():
    today = date.today()
    start = today.replace(day=1)

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": str(start),
            "End": str(today)
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

    return {
        "month": start.strftime("%B"),
        "amount": round(float(amount), 2)
    }


# ==============================
# SERVICE-BY-SERVICE COSTS
# ==============================
def get_service_costs():
    today = date.today()
    start = today.replace(day=1)

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

    results = response["ResultsByTime"][0]["Groups"]

    service_costs = {}

    for item in results:
        service_name = item["Keys"][0]
        amount = item["Metrics"]["UnblendedCost"]["Amount"]

        service_costs[service_name] = round(float(amount), 2)

    return service_costs