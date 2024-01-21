from fastapi import FastAPI
import uvicorn

from database.db import Database

app: FastAPI = FastAPI()

@app.get("/")
async def hello() -> dict:
    return {"message":  "Hello from FastAPI"}

if __name__ == "__main__":
    import sys
    sys.dont_write_bytecode = True
    
    db: Database = Database()
    uvicorn.run(app=app, host="0.0.0.0", port=5050)
