# 3rd party imports
from fastapi import FastAPI
import uvicorn
import sys
# Internal imports
from database.db import Database

# Set global setting to ensure no __pycache__ will be created
sys.dont_write_bytecode = True


def main() -> None:
    app: FastAPI = FastAPI(title="PyProd")
    
    # TODO: Make database object global, to ensure it is accessible
    # in different routes
    db: Database = Database()

    # TODO: Ensure the app is global and add different 
    # blueprints for different urls
    uvicorn.run(app=app, host="0.0.0.0", port=5050)

if __name__ == "__main__":
    main()