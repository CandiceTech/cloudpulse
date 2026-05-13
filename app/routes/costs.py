from fastapi import APIRouter
from app.aws.cost_explorer import (
    get_monthly_costs,
    get_service_costs
)

router = APIRouter(
    prefix="/costs",
    tags=["Costs"]
)


# ==============================
# TOTAL MONTHLY COST
# ==============================
@router.get("/monthly")
def monthly_costs():
    return get_monthly_costs()


# ==============================
# SERVICE COST BREAKDOWN
# ==============================
@router.get("/services")
def service_costs():
    return get_service_costs()