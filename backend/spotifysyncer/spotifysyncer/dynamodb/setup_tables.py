from spotifysyncer.dynamodb.initialize import get_dynamo_db_client
from logging import getLogger

logger = getLogger(__name__)

"""
Creates the initially needed dynamo db table to store spotify user data
"""


def create_user_info_table() -> None:
    dynamodb = get_dynamo_db_client()

    existing_tables = dynamodb.list_tables()

    logger.error(existing_tables)
    logger.error(type(dynamodb))
