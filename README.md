# CloudPulse

CloudPulse is an AWS cloud cost optimization and FinOps visibility platform. I built it to practice cloud engineering with a project that connects to real AWS-style workflows: cost tracking, EC2 utilization, S3 optimization, recommendations, dashboards, Docker, and CI/CD.

The project has a FastAPI backend and a React dashboard. It can run in demo mode with mock AWS data, so the platform is easy to test without needing AWS credentials.

## What CloudPulse Does

CloudPulse helps answer questions like:

- Which EC2 instances look idle or underused?
- How much money could be saved by stopping or downsizing resources?
- Which S3 buckets may need lifecycle policies?
- What are the monthly and annual savings opportunities?
- Which resources should be reviewed first?

## Current Features

- FastAPI backend
- React/Vite frontend dashboard
- Demo mode with realistic mock AWS optimization data
- AWS Cost Explorer integration path
- EC2 utilization and rightsizing recommendations
- S3 optimization recommendations
- Cloud optimization summary endpoint
- Risk levels for resources
- Estimated monthly and annual savings
- Dockerfile for backend containerization
- GitHub Actions CI for backend tests, frontend build, and Docker build

## Tech Stack

Backend:

- Python
- FastAPI
- Boto3
- Pytest

Frontend:

- React
- Vite
- Recharts
- Tailwind/PostCSS

Cloud and DevOps:

- AWS EC2
- AWS CloudWatch
- AWS Cost Explorer
- AWS S3
- Docker
- GitHub Actions

## Project Structure

```text
app/
  aws/
  routes/
  services/
  main.py

cloudpulse/frontend/
  src/
  package.json

tests/
Dockerfile
requirements.txt
```

## Running The Backend

Install dependencies:

```bash
pip install -r requirements.txt
pip install pytest httpx
```

Run the API in demo mode:

```bash
set CLOUDPULSE_USE_MOCKS=true
python -m uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Running The Frontend

```bash
cd cloudpulse/frontend
npm install
npm run dev
```

The frontend expects the backend at:

```text
http://localhost:8000
```

## Demo Mode

By default, CloudPulse uses mock data so the project works without AWS credentials.

```bash
CLOUDPULSE_USE_MOCKS=true
```

To connect to real AWS APIs later, configure AWS credentials and set:

```bash
CLOUDPULSE_USE_MOCKS=false
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | API status |
| `GET` | `/health` | Health check and demo mode status |
| `GET` | `/costs/monthly` | Monthly AWS cost summary |
| `GET` | `/costs/services` | Service-level AWS cost breakdown |
| `GET` | `/ec2/idle` | EC2 utilization and optimization recommendations |
| `GET` | `/s3/analyze` | S3 storage optimization recommendations |
| `GET` | `/analytics/summary` | Combined savings and risk summary |

## Example Optimization Response

```json
{
  "instance_id": "i-0a12cloudpulse001",
  "current_instance_type": "t3.large",
  "recommended_instance_type": "t3.medium",
  "avg_cpu": 2.4,
  "estimated_monthly_cost": 60.0,
  "potential_monthly_savings": 60.0,
  "estimated_annual_savings": 720.0,
  "risk_level": "HIGH",
  "recommendation": "Potentially idle - consider stopping"
}
```

## Testing

Run backend tests:

```bash
pytest -q
```

Run frontend build:

```bash
cd cloudpulse/frontend
npm run build
```

## Docker

Build the backend image:

```bash
docker build -t cloudpulse-api .
```

Run the backend container:

```bash
docker run -p 8000:8000 -e CLOUDPULSE_USE_MOCKS=true cloudpulse-api
```

## CI/CD

The GitHub Actions workflow validates:

- Backend tests
- Frontend production build
- Docker image build

This gives the project a basic DevOps pipeline and keeps the app testable as features are added.

## What I Learned

This project helped me practice AWS cost optimization concepts, API design, frontend/backend integration, mock data for local development, Docker containerization, and CI/CD.

One important improvement was adding demo mode. Without it, the app depends on AWS credentials and live AWS data. With demo mode, the project can be reviewed, tested, and demonstrated anywhere.

## Future Improvements

- Add Terraform AWS infrastructure
- Add authentication
- Add PostgreSQL for storing optimization history
- Add real S3 live analysis
- Add multi-account AWS support
- Add Slack or email alerts
- Add Grafana dashboards
- Add automated remediation workflows

## Author

Candice Scarborough
