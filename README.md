# Web-app | AWS Cloud Automation with Python Scripting and Docker

**ENG MohameNageeb**

## Overview
This project demonstrates the migration and automation of a web application to AWS using Python scripting, Flask, and Docker. Key features include:

- Deployment of Flask web application on AWS EC2
- Containerization with Docker for web app and Redis
- Redis used for database caching to improve performance
- Automation scripts in Python to streamline cloud deployment
- Scalable and reliable infrastructure setup

## Getting Started

### Prerequisites
- Docker & Docker Compose installed
- AWS CLI configured
- Python 3.11+ installed

### Running Locally
```bash
docker-compose up --build
```

Access the web app at `http://localhost:5000`

### Deployment Script
The `scripts/deploy_ec2.py` script is an example placeholder for automating EC2 deployment using Boto3.

## License
MIT License