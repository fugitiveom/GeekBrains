from fastapi import FastAPI
from routers import router as main_router
from db import Base
from manager import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    main_router,
    prefix="",
    tags=["main"]
)
