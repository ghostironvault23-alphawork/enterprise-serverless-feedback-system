# Recruiter Scorecard

## Current Score

**8.2 / 10**

This is a solid AWS serverless portfolio project for entry-level cloud roles. It demonstrates a complete workflow: static frontend, API Gateway, Lambda validation, DynamoDB storage, SNS alerts, IAM-aware access, CloudWatch monitoring, CI validation, and SAM-based deployment.

## Score Breakdown

| Area | Score | Recruiter View |
|---|---:|---|
| Problem clarity | 8.6/10 | Clear business use case: collect feedback without running backend servers. |
| AWS serverless relevance | 8.8/10 | S3, API Gateway, Lambda, DynamoDB, SNS, IAM, and CloudWatch are directly relevant to AWS cloud roles. |
| Code quality | 8.0/10 | Lambda includes validation, error handling, CORS, and email masking. More tests would improve it. |
| Security positioning | 8.1/10 | IAM, CORS, input validation, masking, and production hardening notes are visible. |
| Recruiter readability | 8.5/10 | README, architecture diagram, deployment guide, and pitch make the repo easy to scan. |
| Traffic potential | 7.7/10 | Strong AWS keywords, but screenshots, GitHub topics, and LinkedIn promotion are needed for more visitors. |

## Best Fit Roles

| Role | Match |
|---|---:|
| AWS Cloud Engineer Intern | High |
| Cloud Support Engineer | High |
| Serverless Developer Intern | High |
| Cloud Security Intern | Medium-High |
| Solutions Architect Intern | Medium-High |
| DevOps Intern | Medium |

## Traffic Tracking

Check actual repository traffic here:

```text
GitHub Repo → Insights → Traffic
```

Track these weekly:

| Metric | What to Look For |
|---|---|
| Views | How many times the repo was opened |
| Unique visitors | How many different people viewed it |
| Clones | Whether people are interested enough to test it |
| Referrers | LinkedIn, GitHub search, Google, or direct traffic |
| Popular content | Which files attract the most attention |

## Recommended GitHub Topics

Add these manually from **Repo → Settings → Topics**:

```text
aws
serverless
lambda
api-gateway
dynamodb
sns
s3
cloudwatch
iam
cloud-engineering
cloud-security
aws-project
feedback-system
```

## Necessary Next Improvements

Do not over-edit the README now. The next changes that will actually improve recruiter trust are:

1. Add 3 to 5 real AWS console screenshots.
2. Add one API success screenshot showing `feedbackId` generated.
3. Add one DynamoDB screenshot showing saved feedback.
4. Add one CloudWatch screenshot showing Lambda logs.
5. Pin this repo on your GitHub profile.
6. Share a LinkedIn post with the architecture image and repo link.

## Next Improvement to Reach 9/10

- Add real AWS console screenshots.
- Add a short demo video/GIF.
- Add CloudFront + WAF as production extension.
- Add unit tests with mocked DynamoDB and SNS clients.
- Add CloudWatch alarm examples.
