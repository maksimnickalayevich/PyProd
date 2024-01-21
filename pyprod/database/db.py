from psycopg2.pool import ThreadedConnectionPool

from configs.db_config import DbConfig


class Database:
    config: DbConfig
    pool: ThreadedConnectionPool
    
    def __init__(self) -> None:
        self.config = DbConfig()
        self.connection_uri = DbConfig.compose_db_uri()
        self.pool = ThreadedConnectionPool(
            minconn=1,
            maxconn=self.config.max_connections,
            dsn=self.connection_uri
        )

    def connect(self) -> None:
        """
        Makes connection to the database based on the config
        """

    