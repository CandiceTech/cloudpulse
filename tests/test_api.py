from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ec2_idle_endpoint_returns_demo_instances():
    response = client.get("/ec2/idle")

    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 1
    assert body[0]["instance_id"]
    assert body[0]["risk_level"] in ["LOW", "MEDIUM", "HIGH"]


def test_analytics_summary_returns_savings():
    response = client.get("/analytics/summary")

    assert response.status_code == 200
    body = response.json()
    assert body["instances_analyzed"] >= 1
    assert body["total_monthly_savings"] > 0
    assert body["total_annual_savings"] > 0


def test_s3_analyze_endpoint_returns_buckets():
    response = client.get("/s3/analyze")

    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 1
    assert body[0]["bucket_name"]
