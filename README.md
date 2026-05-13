# CloudPulse

CloudPulse is an AWS cloud cost optimization platform built to help identify underutilized infrastructure, reduce unnecessary cloud spending, and provide better visibility into AWS resource usage.

I originally started this project to get more hands-on experience with AWS, cloud operations, and backend engineering while building something that solves a real business problem.

Instead of creating another basic CRUD app, I wanted to build a platform that interacts directly with AWS services and provides meaningful operational insights.

---

# What CloudPulse Does

CloudPulse currently:

* Pulls AWS billing data using the Cost Explorer API
* Displays service-level AWS spending
* Detects potentially idle EC2 instances
* Analyzes CloudWatch CPU utilization metrics
* Estimates monthly and annual savings opportunities
* Generates infrastructure optimization recommendations
* Assigns risk levels based on utilization patterns

---

# Current Features

## AWS Cost Explorer Integration

Retrieve:

* Monthly AWS costs
* Service-by-service spending breakdowns

### Example Endpoint

```bash
/costs/monthly
/costs/services
```

---

## EC2 Optimization Engine

Analyze EC2 usage and identify low-utilization resources.

### Features

* EC2 instance discovery
* CPU utilization analysis
* Estimated monthly costs
* Potential savings calculations
* Rightsizing recommendations
* Risk scoring

### Example Response

```json
[
  {
    "instance_id": "i-123456",
    "current_instance_type": "t3.micro",
    "recommended_instance_type": "t3.micro",
    "avg_cpu": 1.69,
    "estimated_monthly_cost": 8.5,
    "potential_monthly_savings": 8.5,
    "estimated_annual_savings": 102,
    "risk_level": "HIGH",
    "recommendation": "Potentially idle - consider stopping"
  }
]
```

---

# Tech Stack

## Backend

* Python
* FastAPI
* Boto3

## AWS Services

* EC2
* CloudWatch
* Cost Explorer API
* IAM

## Planned Infrastructure

* Docker
* Kubernetes
* Terraform
* PostgreSQL
* Grafana

---

# Project Structure

```bash
backend/
│
├── app/
│   ├── aws/
│   ├── routes/
│   ├── services/
│   └── main.py
│
├── requirements.txt
├── Dockerfile
└── .env
```

---

# Running the Project

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/cloudpulse.git
```

## Navigate Into the Project

```bash
cd cloudpulse
```

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure AWS Credentials

Install the AWS CLI and run:

```bash
aws configure
```

You will need:

* AWS Access Key
* AWS Secret Access Key
* Default region

---

# Start the API

```bash
python -m uvicorn app.main:app --reload
```

Swagger documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# Why I Built This

One thing I noticed while learning cloud engineering is that companies often waste money on infrastructure simply because they lack visibility.

Idle EC2 instances, forgotten resources, and oversized infrastructure can quietly increase monthly cloud bills.

I built CloudPulse to better understand:

* AWS infrastructure APIs
* CloudWatch metrics
* cloud cost optimization
* backend architecture
* operational tooling
* FinOps concepts

This project has also helped me get more practical experience working with real AWS services instead of only following tutorials.

---

# Roadmap

Planned features:

* Docker containerization
* React frontend dashboard
* Authentication and RBAC
* PostgreSQL integration
* Terraform support
* Multi-account AWS support
* Automated remediation
* Slack/email alerts
* Grafana dashboards
* Kubernetes deployment
* CI/CD pipelines

---

# Future Goals

The long-term goal is to evolve CloudPulse into a more complete cloud operations and FinOps platform capable of:

* identifying cloud waste
* monitoring infrastructure health
* improving operational visibility
* helping teams optimize AWS spending

---

# Author

Built by Candy Scar
