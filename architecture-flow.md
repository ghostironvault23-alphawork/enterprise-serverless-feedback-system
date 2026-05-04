# Architecture Flow

```text
User
  |
  v
S3 Static Website
  |
  v
API Gateway HTTP API
  |
  v
Lambda Function
  |
  +----> DynamoDB Table
  |
  +----> SNS Notification
  |
  v
CloudWatch Logs
```

## Flow Explanation

1. User submits feedback from the frontend.
2. API Gateway receives the request.
3. Lambda processes the feedback.
4. DynamoDB stores the record.
5. SNS sends notification.
6. CloudWatch stores execution logs.
