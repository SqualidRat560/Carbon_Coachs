from __future__ import annotations

from fastapi import FastAPI

from api.routes import router
from db.database import init_db

app = FastAPI(title="Carbon Coach API", version="0.1.0")
app.include_router(router)


@app.on_event("startup")
def startup() -> None:
    init_db()
