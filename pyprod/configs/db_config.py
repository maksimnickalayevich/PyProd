import os
from dotenv import load_dotenv

from errors.utilities import (
    handle_none_value, 
    handle_none_values
)
from constants import DbContants


class DbConfig:
    host: str
    username: str
    pswd: str
    db_name: str
    port: str
    max_connections: int
    
    def __init__(self) -> None:
        self.load_from_env()
    
    @classmethod
    def load_from_env(cls) -> None:
        load_dotenv()
        
        host: str | None = os.getenv(key=DbContants.HOST)
        username: str | None = os.getenv(key=DbContants.USERNAME)
        pswd: str | None = os.getenv(key=DbContants.PSWD)
        port: str | None = os.getenv(key=DbContants.PORT)
        max_conn: int | None = os.getenv(key=DbContants.MAX_CONN)
        db_name: str | None = os.getenv(key=DbContants.NAME)
        
        handle_none_values(values=[host, username, pswd, port, max_conn, db_name])
        print(f" host={host},\n username={username},\n pswd={pswd},\n port={port},\n max_conn={max_conn},\n name={db_name}\n")
        cls.host = host
        cls.port = port
        cls.username = username
        cls.pswd = pswd
        cls.db_name = db_name
        cls.max_connections = max_conn
        
        return None
    
    @classmethod
    def compose_db_uri(cls) -> str:
        """
        Makes a database connection uri based on the values that are
        read from the environment
        @return: composed uri
        """
        return f"postgres://{cls.username}:{cls.pswd}@{cls.host}:{cls.port}/{cls.db_name}"
        