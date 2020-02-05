def hello(event, context):
    print(f"Event : {event}")
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
