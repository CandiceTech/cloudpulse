from fastapi import APIRouter

from app.aws.s3_analyzer import analyze_s3_buckets

router = APIRouter(
    prefix="/s3",
    tags=["S3 Optimization"]
)


@router.get("/analyze")
def s3_analysis():
    return analyze_s3_buckets()
