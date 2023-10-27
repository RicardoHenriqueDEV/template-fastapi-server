import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from routes.main import main_routes

load_dotenv()
PORT = int(os.getenv("PORT"))
PROJECT_NAME = os.getenv("PROJECT_NAME")

app = FastAPI(
    title=PROJECT_NAME,
    description="This api was made to demonstrate how to implement a simple api server with FastAPI.",
    version="1.0.0"
)

app.include_router(main_routes)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="::", port=PORT, reload=True)