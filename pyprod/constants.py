from enum import StrEnum


class DbContants(StrEnum):
    HOST: str = "DB_HOST"
    USERNAME: str = "DB_USERNAME"
    PSWD: str = "DB_PASSWORD"
    NAME: str = "DB_NAME"
    PORT: str = "DB_PORT"
    MAX_CONN: str = "DB_MAX_CONNECTIONS"
