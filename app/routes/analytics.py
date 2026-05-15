from fastapi import APIRouter

from app.services.analytics import get_optimization_summary

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
def optimization_summary():
    return get_optimization_summary()
