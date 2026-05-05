import logging
import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models import cash_flow


class DatabaseSessionManager:
    """
    Class to manage the database session.
    Methods:
        get_session(): Returns a new database session.

    """

    def __init__(self, db_url: str):
        self.engine = create_engine(
            db_url, pool_size=10, pool_pre_ping=True, echo=False
        )

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        self.logger = logging.getLogger(__name__)

    def get_session(self):
        """
        Returns:
            Session: A new database session.
        """
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def init_db(self) -> None:
        """
        Initializes the database by creating all tables defined in the models.
        """
        # Import models to register them with SQLAlchemy
        self.logger.info("init_db called; engine=%s", self.engine.url)
        for attempt in range(10):
            try:
                cash_flow.Base.metadata.create_all(bind=self.engine)
                self.logger.info("Database tables created successfully")
                break
            except OperationalError as e:
                if attempt == 9:
                    raise
                print(f"DB not ready (attempt {attempt + 1}/10), retrying in 3s... {e}")
                time.sleep(3)

        self.logger.info("create_all finished")


# Create instance
db_manager = DatabaseSessionManager(settings.DATABASE_URL)
