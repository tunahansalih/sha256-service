import os
import boto3

DB_REGION_NAME = os.getenv('DB_REGION_NAME')
DB_ACCESS_KEY_ID = os.getenv('DB_ACCESS_KEY_ID')
DB_SECRET_ACCESS_KEY = os.getenv('DB_SECRET_ACCESS_KEY')

def initialize_db():
    ddb = boto3.resource('dynamodb',
                         region_name=DB_REGION_NAME,
                         aws_access_key_id=DB_ACCESS_KEY_ID,
                         aws_secret_access_key=DB_SECRET_ACCESS_KEY)
    try:
        table = ddb.Table('messages')
        table.load()
    except:
        table = ddb.create_table(
            TableName='messages',
            KeySchema=[
                {
                    'AttributeName': 'hash',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'hash',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        table.wait_until_exists()
    return table