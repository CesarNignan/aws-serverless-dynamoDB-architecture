import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Customers")


def lambda_handler(event, context):
    try:
        data = json.loads(event.get("body") or "{}")
        item = {
            "CustomerID": int(data["CustomerID"]),  # PK (Number)
            "OrderID": int(data["OrderID"]),        # SK (Number)
            "Name": data["Name"],
            "Email": data["Email"],
        }
    except (KeyError, ValueError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid or missing fields"}),
        }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Record written", "item": item}),
    }