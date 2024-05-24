import os
import boto3
import json

QUEUE_URL = os.getenv("QUEUE_URL", default="test")
sqs = boto3.client('sqs')

# Function to send the message to SQS
def send_message_to_sqs(body):
    print('Sending message to SQS')
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(body)
    )
    
# Function to test if a string is a US zip code
def validate_zip(zip):
    if len(zip) == 5:
        if zip.isdigit():
            return True
    return False

# Lambda function to publish Users to a queue
def lambda_handler(event, context):
    print(event)
    try:
        body = json.loads(event['body'])
        
        # Validate the zip code
        if not validate_zip(body['zip']):
            return {'statusCode': 400}
        
        send_message_to_sqs(body)
        return {'statusCode': 200}
    except Exception as e:
        print(e)
        return {'statusCode': 500}