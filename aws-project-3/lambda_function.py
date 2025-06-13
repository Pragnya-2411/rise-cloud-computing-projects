import json

def lambda_handler(event, context):
    print("Incoming event:", event)
    # Handle CORS preflight request
    if event['requestContext']['http']['method'] == 'OPTIONS':
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            }
        }

    try:
        body = json.loads(event['body'])
        name = body.get("name")
        email = body.get("email")
        message = body.get("message")

        print(f"New contact form submission:\nName: {name}\nEmail: {email}\nMessage: {message}")

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"message": "Form submitted successfully!"})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"error": "Internal server error."})
        }