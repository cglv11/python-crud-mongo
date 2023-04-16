from fastapi import FastAPI
from routes.user import user
from docs import tags_metada

app = FastAPI(
    title="REST API with FastAPI and mongodb",
    description="This is a simple rest api with fastAPI",
    version="0.0.1",
    openapi_tags=tags_metada
)

app.include_router(user)