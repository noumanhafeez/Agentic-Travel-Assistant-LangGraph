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

        logger.error(
            "DATABASE_URL not found"
        )

        raise ValueError(
            "DATABASE_URL is missing in .env"
        )

    try:

        conn = psycopg.connect(
            database_url
        )

        logger.info(
            "PostgreSQL connected successfully"
        )

        saver = PostgresSaver(
            conn
        )

        saver.setup()

        logger.info(
            "LangGraph checkpoint initialized"
        )

        return saver

    except psycopg.OperationalError as e:

        logger.exception(
            "Database connection failed"
        )

        raise RuntimeError(
            f"Unable to connect to PostgreSQL: {e}"
        )

    except Exception as e:

        logger.exception(
            "Unexpected checkpoint error"
        )

        raise RuntimeError(
            f"Checkpoint initialization failed: {e}"
        )