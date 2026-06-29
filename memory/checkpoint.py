import os
import logging
import psycopg

from dotenv import load_dotenv
from langgraph.checkpoint.postgres import (
    PostgresSaver
)

load_dotenv()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_checkpointer():

    database_url = os.getenv(
        "DATABASE_URL"
    )

    if not database_url:

        raise ValueError(
            "DATABASE_URL missing"
        )

    try:

        conn = psycopg.connect(
            database_url,
            autocommit=True
        )

        logger.info(
            "PostgreSQL connected successfully"
        )

        saver = PostgresSaver(
            conn
        )

        saver.setup()

        logger.info(
            "Checkpoint initialized successfully"
        )

        return saver

    except psycopg.OperationalError as e:

        logger.exception(
            "Database connection failed"
        )

        raise RuntimeError(
            f"Unable to connect: {e}"
        )

    except Exception as e:

        logger.exception(
            "Unexpected checkpoint error"
        )

        raise RuntimeError(
            f"Checkpoint initialization failed: {e}"
        )