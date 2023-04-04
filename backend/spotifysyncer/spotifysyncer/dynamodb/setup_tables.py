from spotifysyncer.dynamodb.initialize import get_dynamo_db_client
from logging import getLogger

logger = getLogger(__name__)

"""
Creates the initially needed dynamo db table to store spotify user data
"""


def create_user_info_table() -> None:
    dynamodb = get_dynamo_db_client()

    existing_tables = dynamodb.list_tables()

    if len(existing_tables["TableNames"]) > 0:
        logger.info(f"Already existing tables: {[table for table in existing_tables['TableNames']]}")
        logger.info("No table needed to be created")
        return

    table_created_response = dynamodb.create_table(
        TableName="Users",
        KeySchema=[
            {
                "AttributeName": "user_id",
                "KeyType": "HASH"
            }
        ],
       AttributeDefinitions=[
           {
               "AttributeName": "user_id",
               "AttributeType": "N"
           }
       ],
        BillingMode="PAY_PER_REQUEST"
    )

    logger.info(table_created_response)
