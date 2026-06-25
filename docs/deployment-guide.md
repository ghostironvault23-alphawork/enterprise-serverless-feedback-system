# Deployment Guide

This guide explains the clean deployment flow for the Enterprise Serverless Feedback System.

## AWS Services

| Layer | Service |
|---|---|
| Frontend | Amazon S3 Static Website Hosting |
| API | Amazon API Gateway HTTP API |
| Backend | AWS Lambda |
| Database | Amazon DynamoDB |
| Notification | Amazon SNS |
| Monitoring | Amazon CloudWatch |
| Security | IAM, environment variables, CORS controls |

## Console Deployment Flow

1. Create an S3 bucket and enable static website hosting.
2. Upload `frontend/index.html`, `frontend/style.css`, and `frontend/app.js`.
3. Create a DynamoDB table named `FeedbackTable` with partition key `feedbackId`.
4. Create an SNS topic and confirm your email subscription.
5. Create a Lambda execution role with least-privilege access to DynamoDB, SNS, and CloudWatch Logs.
6. Create the Lambda function using `lambda/handler.py`.
7. Add Lambda environment variables:

```text
DYNAMODB_TABLE=FeedbackTable
SNS_TOPIC_ARN=<your-sns-topic-arn>
ALLOWED_ORIGIN=<your-s3-website-origin-or-*>
```

8. Create an API Gateway HTTP API with `POST /feedback` route.
9. Connect the route to Lambda.
10. Copy the API Gateway invoke URL into `frontend/app.js` as `API_ENDPOINT`.
11. Submit feedback from the frontend and verify:
    - DynamoDB item is created
    - SNS email is received
    - CloudWatch logs show successful processing

## SAM Deployment

```bash
cd infrastructure/aws-sam
sam build
sam deploy --guided
```

After deployment, use the `FeedbackApiUrl` output as the frontend API endpoint.

## Production Hardening

- Replace public S3 hosting with CloudFront + Origin Access Control.
- Restrict CORS to the exact frontend domain.
- Use least-privilege IAM policies instead of broad managed policies.
- Add API throttling and WAF for abuse protection.
- Enable DynamoDB point-in-time recovery.
- Add CloudWatch alarms for Lambda errors and API 5xx responses.
