from botocore.exceptions import ClientError

from .. import schemas


def get_message(table, hash: str):
    try:
        response = table.get_item(Key={'hash': hash})
        if 'Item' in response:
            return schemas.MessageHash(**response['Item'])
        else:
            return None
    except ClientError as e:
        raise ValueError(e.response['Error']['Message'])


def create_message(table, message: schemas.MessageHash):
    try:
        table.put_item(Item=message.dict())
    except ClientError as e:
        raise ValueError(e.response['Error']['Message'])

