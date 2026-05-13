from fastapi import APIRouter
from app.aws.ec2_analyzer import get_idle_instances

router = APIRouter(
    prefix="/ec2",
    tags=["EC2 Optimization"]
)


@router.get("/idle")
def idle_instances():
    return get_idle_instances()