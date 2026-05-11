from fastapi import FastAPI
from app.routes.costs import router as costs_router
from app.routes.ec2 import router as ec2_router

app = FastAPI(
    title="CloudPulse API",
    version="1.0.0"
)

app.include_router(costs_router)
app.include_router(ec2_router)

@app.get("/")
def root():
    return {"message": "CloudPulse API Running"}