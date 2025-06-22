from fastapi import FastAPI
import asyncio
from app.services.scheduler import start_scheduler
from app.routers import reservation, salle

app = FastAPI(
    title="A simple WMS",
    description="A simple WMS REST API built with FastAPI, SQLAlchemy, and SQLite",
    version="0.1.0",
)

app.include_router(reservation.router)
app.include_router(salle.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SimpleWMS!"}

@app.on_event("startup")
async def startup_event():
    # Start the background scheduler
    await asyncio.create_task(start_scheduler())
    print("Scheduler started.")
