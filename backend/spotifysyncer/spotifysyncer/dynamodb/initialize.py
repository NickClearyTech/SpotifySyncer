import boto3

from settings import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, AWS_DYNAMODB_ENDPOINT_URL, AWS_REGION

def get_dynamo_db_resource():
    return boto3.resource('dynamodb',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=AWS_REGION,
                            endpoint_url=AWS_DYNAMODB_ENDPOINT_URL)

def get_dynamo_db_client():
    return boto3.client("dynamodb",
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=AWS_REGION,
                            endpoint_url=AWS_DYNAMODB_ENDPOINT_URL)