import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

logger = logging.getLogger("audit")


def audit_event(message):
    """
    Logs security-related events without exposing secrets.
    """
    logger.info(message)
def log_secret_access(user, secret_id):

    logger.info(
        f"SECRET_ACCESS user={user} secret={secret_id}"
    )


def log_share_created(user, secret_id):

    logger.info(
        f"SHARE_CREATED user={user} secret={secret_id}"
    )


def log_share_consumed(token):

    logger.info(
        f"SHARE_CONSUMED token={token}"
    )


def log_failed_access(user):

    logger.warning(
        f"FAILED_ACCESS user={user}"
    )
    