import json
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Tuple

import boto3

DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE", "FeedbackTable")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN", "")
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "*")

_dynamodb = boto3.resource("dynamodb")
_sns = boto3.client("sns")
_table = _dynamodb.Table(DYNAMODB_TABLE)

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Process feedback from API Gateway and store it in DynamoDB.

    Expected JSON body:
    {
      "name": "User Name",
      "email": "user@example.com",
      "rating": 5,
      "message": "Great service"
    }
    """
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return build_response(204, {})

    try:
        body = parse_body(event)
        is_valid, error_message = validate_feedback(body)
        if not is_valid:
            return build_response(400, {"message": error_message})

        feedback_id = str(uuid.uuid4())
        item = {
            "feedbackId": feedback_id,
            "name": body["name"].strip(),
            "email": body["email"].strip().lower(),
            "rating": int(body["rating"]),
            "message": body["message"].strip(),
            "source": body.get("source", "web-form"),
            "createdAt": datetime.now(timezone.utc).isoformat(),
        }

        _table.put_item(Item=item)
        publish_notification(item)

        return build_response(
            200,
            {
                "message": "Feedback submitted successfully",
                "feedbackId": feedback_id,
            },
        )
    except json.JSONDecodeError:
        return build_response(400, {"message": "Invalid JSON body"})
    except Exception as exc:
        print(f"Unhandled error: {exc}")
        return build_response(500, {"message": "Internal server error"})


def parse_body(event: Dict[str, Any]) -> Dict[str, Any]:
    body = event.get("body", {})
    if isinstance(body, dict):
        return body
    return json.loads(body or "{}")


def validate_feedback(body: Dict[str, Any]) -> Tuple[bool, str]:
    required = ["name", "email", "rating", "message"]
    missing = [field for field in required if not body.get(field)]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    if not EMAIL_PATTERN.match(str(body["email"])):
        return False, "Invalid email address"

    try:
        rating = int(body["rating"])
    except (TypeError, ValueError):
        return False, "Rating must be a number between 1 and 5"

    if rating < 1 or rating > 5:
        return False, "Rating must be between 1 and 5"

    if len(str(body["message"]).strip()) < 5:
        return False, "Message must contain at least 5 characters"

    return True, "valid"


def publish_notification(item: Dict[str, Any]) -> None:
    if not SNS_TOPIC_ARN:
        return

    safe_item = dict(item)
    safe_item["email"] = mask_email(safe_item["email"])

    _sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="New Feedback Received",
        Message=json.dumps(safe_item, indent=2),
    )


def mask_email(email: str) -> str:
    name, _, domain = email.partition("@")
    if len(name) <= 2:
        return f"**@{domain}"
    return f"{name[0]}***{name[-1]}@{domain}"


def build_response(status_code: int, body: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
        },
        "body": json.dumps(body),
    }
