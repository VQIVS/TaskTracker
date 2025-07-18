from fastapi import FastAPI
from routers.task_router import router as task_router

app = FastAPI()

app.include_router(task_router)
