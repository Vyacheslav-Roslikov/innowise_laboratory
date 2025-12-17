from contextlib import asynccontextmanager
from database import engine, Model
from routers.book import router as book_router
from fastapi import FastAPI
from models.books import Book


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables.")
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    print("Tables created.")
    yield
    print("App stopped.")

app = FastAPI(lifespan=lifespan, title="Book API")
app.include_router(book_router)

@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}