# Enterprise-Level Serverless Feedback Collection System

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![S3](https://img.shields.io/badge/Amazon-S3-green)
![API Gateway](https://img.shields.io/badge/API-Gateway-purple)
![Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![DynamoDB](https://img.shields.io/badge/DynamoDB-blue)
![SNS](https://img.shields.io/badge/SNS-pink)
![IAM](https://img.shields.io/badge/IAM-red)
![CloudWatch](https://img.shields.io/badge/CloudWatch-yellow)

## Project Summary

This project is an enterprise-style **serverless feedback collection system** built on AWS. It collects user feedback through a static web form hosted on **Amazon S3**, sends the request to **Amazon API Gateway**, processes it using **AWS Lambda**, stores the record in **Amazon DynamoDB**, and sends notifications using **Amazon SNS**. **Amazon CloudWatch** is used for logs and troubleshooting, while **AWS IAM** manages service permissions securely.

This repository is written and organized like a professional cloud engineering portfolio project.

---

## Problem Statement

Organizations need a simple, scalable, and low-maintenance way to collect feedback from users without managing servers. Traditional systems require backend servers, database maintenance, manual scaling, and separate monitoring setup. This project solves that using AWS serverless services.

---

## Architecture Diagram

<img src="architecture/serverless-feedback-architecture.svg" width="950" alt="Serverless Feedback Collection System Architecture">

---

## Architecture Flow

```text
User
  |
  v
Amazon S3 Static Website
  |
  v
Amazon API Gateway
  |
  v
AWS Lambda
  |
  +------------------> Amazon DynamoDB
  |
  +------------------> Amazon SNS
  |
  v
Amazon CloudWatch Logs
```

---

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Hosts the static frontend feedback form |
| Amazon API Gateway | Provides the HTTP POST endpoint |
| AWS Lambda | Processes, validates, and routes feedback data |
| Amazon DynamoDB | Stores feedback records |
| Amazon SNS | Sends email/SMS notifications |
| AWS IAM | Controls permissions using roles and policies |
| Amazon CloudWatch | Captures logs, errors, and runtime details |

---

## Tools and Software Used

| Tool | Purpose |
|---|---|
| AWS Management Console | GUI-based cloud deployment |
| VS Code | Code editing |
| GitHub | Version control and documentation |
| Postman | API testing |
| Browser Developer Tools | Frontend validation |
| CloudWatch Logs | Debugging and monitoring |

---

## Repository Structure

```text
enterprise-serverless-feedback-system/
├── README.md
├── architecture/
│   ├── serverless-feedback-architecture.svg
│   ├── solution-overview.md
│   ├── architecture-flow.md
│   └── future-scope.md
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── lambda/
│   ├── handler.py
│   └── requirements.txt
├── docs/
│   ├── github-upload-steps.md
│   ├── gui-step-by-step.md
│   ├── deployment-guide.md
│   ├── testing-checklist.md
│   └── troubleshooting.md
├── monitoring/
│   └── cloudwatch-dashboard.md
├── screenshots/
│   ├── s3-hosting-sample.svg
│   ├── api-gateway-sample.svg
│   ├── lambda-console-sample.svg
│   ├── dynamodb-table-sample.svg
│   └── cloudwatch-logs-sample.svg
└── postman/
    └── feedback-api-collection.json
```

---

## Project Workflow

1. User opens the feedback form hosted on Amazon S3.
2. User submits name, email, rating, and message.
3. Frontend sends the request to API Gateway.
4. API Gateway triggers the Lambda function.
5. Lambda validates the request payload.
6. Lambda stores the feedback record in DynamoDB.
7. Lambda publishes a notification to SNS.
8. Admin receives an email/SMS notification.
9. CloudWatch stores execution logs for monitoring and troubleshooting.

---

## Documentation

- [GUI Step-by-Step Guide](docs/gui-step-by-step.md)
- [Deployment Guide](docs/deployment-guide.md)
- [Testing Checklist](docs/testing-checklist.md)
- [Troubleshooting Guide](docs/troubleshooting.md)
- [Future Scope](architecture/future-scope.md)
- [CloudWatch Monitoring Plan](monitoring/cloudwatch-dashboard.md)

---

## Project Screenshots

### S3 Static Website Hosting
<img src="screenshots/s3-hosting-sample.svg" width="750" alt="S3 screenshot placeholder">

### API Gateway Endpoint
<img src="screenshots/api-gateway-sample.svg" width="750" alt="API Gateway screenshot placeholder">

### Lambda Function Console
<img src="screenshots/lambda-console-sample.svg" width="750" alt="Lambda screenshot placeholder">

### DynamoDB Table
<img src="screenshots/dynamodb-table-sample.svg" width="750" alt="DynamoDB screenshot placeholder">

### CloudWatch Logs
<img src="screenshots/cloudwatch-logs-sample.svg" width="750" alt="CloudWatch screenshot placeholder">

---

## Individual Contribution

This project was completed as a self-driven cloud engineering project.

My contribution includes:

- Planned the serverless architecture end-to-end
- Configured AWS services using the AWS Management Console
- Built the frontend feedback form
- Developed Lambda backend processing logic
- Integrated API Gateway with Lambda
- Created DynamoDB storage for feedback records
- Configured SNS notification workflow
- Applied IAM permissions for AWS service access
- Tested the application using browser and Postman
- Documented the complete GitHub project professionally

---

## Future Improvements

| Improvement | Purpose |
|---|---|
| Amazon Cognito | Add secure user authentication |
| AWS WAF | Protect API from common web attacks |
| AWS Shield | Add DDoS protection |
| Amazon Kinesis | Enable real-time analytics |
| Amazon Aurora | Add relational reporting support |
| Amazon QuickSight | Build dashboards and insights |
| AWS Step Functions | Orchestrate complex workflows |
| GitHub Actions / CodePipeline | Automate CI/CD deployment |
| Amazon Comprehend | Add sentiment analysis |

---

## Resume-Ready Description

Designed and implemented an enterprise-level serverless feedback collection system using AWS S3, API Gateway, Lambda, DynamoDB, SNS, IAM, and CloudWatch. Built a static frontend hosted on Amazon S3, integrated it with API Gateway and Lambda for backend processing, stored feedback data in DynamoDB, and configured SNS for real-time notifications. Applied IAM-based access control and used CloudWatch for logging, monitoring, and troubleshooting.
