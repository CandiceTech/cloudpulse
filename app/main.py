from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import use_mock_data
from app.routes.analytics import router as analytics_router
from app.routes.costs import router as costs_router
from app.routes.ec2 import router as ec2_router
from app.routes.s3 import router as s3_router

app = FastAPI(
    title="CloudPulse API",
    version="1.0.0",
    description="AWS cloud optimization and FinOps visibility API."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(costs_router)
app.include_router(ec2_router)
app.include_router(analytics_router)
app.include_router(s3_router)

@app.get("/")
def root():
    return {
        "message": "CloudPulse API Running",
        "demo_mode": use_mock_data(),
        "docs_url": "/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloudpulse-api",
        "demo_mode": use_mock_data()
    }
