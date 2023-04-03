from django.contrib.auth.models import User
from oauth2_provider.models import Application
from settings import *

from spotifysyncer.dynamodb.setup_tables import create_user_info_table

from logging import getLogger

logger = getLogger(__name__)


def check_and_create_initial_superuser() -> None:
    if (
        User.objects.filter(is_superuser=True, username=INITIAL_USER_USERNAME).count()
        >= 1
    ):
        logger.info("Initial superuser exists, continuing")
        return
    superuser = User(
        username=INITIAL_USER_USERNAME,
        first_name=INITIAL_USER_FIRSTNAME,
        last_name=INITIAL_USER_LASTNAME,
        email=INITIAL_USER_EMAIL,
        is_superuser=True,
    )
    superuser.save()
    logger.info("Initial superuser created")


def check_and_create_oauth_application() -> None:
    if (
        Application.objects.filter(
            client_type="public",
            authorization_grant_type="password",
            user_id=1,
            client_id=INITIAL_OAUTH_CLIENT_ID,
        ).count()
        >= 1
    ):
        logger.info("Initial OAuth application exists, continuing")
        return
    application = Application(
        client_type="public",
        authorization_grant_type="password",
        user_id=1,
        client_id=INITIAL_OAUTH_CLIENT_ID,
    )
    application.save()
    logger.info("Initial OAuth application created")


def run_dynamodb_migrations():
    create_user_info_table()
