import json
import boto3


def viewer(name):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="https://dynamodb.ap-northeast-1.amazonaws.com")
    table = dynamodb.Table('questionnaire')

    item = {}
    try:
        response = table.get_item(Key={'name': name})

        print(response)
        item = response['Item'] if ('Item' in response) else {}
    except Exception as e:
        print('get item')
        print(e)

    if item != None and len(item) > 0:
        print('changed')
        item['infra_skill'] = int(item['infra_skill'])
        item['poll_count'] = int(item['poll_count'])
        item['pg_skill'] = int(item['pg_skill'])
        item['op_skill'] = int(item['op_skill'])
        item['comm_skill'] = int(item['comm_skill'])
        item['strength'] = int(item['strength'])
        item['management'] = int(item['management'])
        item['kindness'] = int(item['kindness'])

    return item


def lambda_handler(event, context):
    name = event['queryStringParameters']['name']
    print('name='+name)

    item = viewer(name)
    print(item)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(item),
    }
