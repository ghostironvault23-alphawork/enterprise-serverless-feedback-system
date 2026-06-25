# Deployment Proof Screenshots

Add real AWS screenshots in this folder after deployment. Do not use mock screenshots for recruiter proof.

## Required Screenshots

| File Name | Screenshot To Capture | What Recruiter Should See |
|---|---|---|
| `01-s3-static-website.png` | S3 bucket static website hosting page | Static hosting enabled and website endpoint visible |
| `02-api-gateway-feedback-route.png` | API Gateway route/invoke URL | `POST /feedback` route connected to Lambda |
| `03-api-success-response.png` | Postman/cURL/browser API test | Successful response with generated `feedbackId` |
| `04-dynamodb-saved-item.png` | DynamoDB table item view | Feedback record saved with `feedbackId`, rating, message, createdAt |
| `05-cloudwatch-lambda-logs.png` | CloudWatch log stream | Lambda execution log showing successful processing |
| `06-sns-email-alert.png` | Email inbox or SNS delivery proof | New feedback notification received |

## Screenshot Rules

- Hide or blur AWS account ID, email address, API keys, and exact ARNs if needed.
- Keep the service name visible at the top of the AWS console.
- Keep timestamps visible if possible.
- Use PNG format for best GitHub display.
- Add screenshots only after a real deployment test.

## Recommended README Order

1. API success response
2. DynamoDB saved item
3. CloudWatch Lambda logs
4. S3 static website hosting
5. API Gateway route
6. SNS email alert
