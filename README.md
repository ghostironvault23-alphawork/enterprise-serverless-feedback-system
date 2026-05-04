# enterprise-serverless-feedback-system
Enterprise-level AWS serverless feedback collection system using S3, API Gateway, Lambda, DynamoDB, SNS, IAM, and CloudWatch.

# Enterprise-Level Serverless Feedback Collection System

## Project Summary

This project is an enterprise-style serverless feedback collection system built using AWS services.  
The main goal of this project is to collect user feedback from a web form, process it securely using AWS Lambda, store the data in Amazon DynamoDB, and send real-time notifications using Amazon SNS.

The project follows a fully serverless architecture, which means there is no need to manage physical servers, operating systems, patching, or backend infrastructure manually.

This project was designed, configured, tested, and documented independently to demonstrate practical AWS cloud engineering skills.

---

## What Problem Are We Solving?

Many organizations need a simple, scalable, and secure way to collect feedback from customers, employees, or users.

Traditional applications usually require:

- Server setup
- Backend maintenance
- Manual scaling
- Database administration
- Monitoring setup
- Security configuration

This project solves the problem by using AWS serverless services.

The system allows users to submit feedback through a static web form hosted on Amazon S3. The submitted feedback is sent to API Gateway, processed by Lambda, stored in DynamoDB, and alerts are triggered using SNS.

---

## Project Objectives

The main objectives of this project are:

- Build a serverless feedback collection application
- Host a static frontend using Amazon S3
- Create a secure API using Amazon API Gateway
- Process feedback data using AWS Lambda
- Store feedback records in Amazon DynamoDB
- Send email or SMS alerts using Amazon SNS
- Monitor logs and errors using Amazon CloudWatch
- Apply IAM-based least privilege access
- Create clean documentation suitable for GitHub and portfolio use

---

## Architecture Overview

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
