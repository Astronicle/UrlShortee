import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):

    short_id = event['pathParameters']['shortId']

    response = table.get_item(
        Key={
            'shortId': short_id
        }
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'body': 'URL not found'
        }

    return {
        'statusCode': 301,
        'headers': {
            'Location': item['longUrl']
        }
    }