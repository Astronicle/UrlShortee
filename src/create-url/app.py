import json
import boto3
import os
import secrets
import string
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

alphabet = string.ascii_letters + string.digits

def generate_id(length=6):
    return ''.join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

def lambda_handler(event, context):

    body = json.loads(event['body'])
    long_url = body['url']

    short_id = generate_id()

    table.put_item(
        Item={
            'shortId': short_id,
            'longUrl': long_url,
            'createdAt': datetime.utcnow().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'shortId': short_id
        })
    }