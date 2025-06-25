from fastapi import FastAPI
import asyncio
from fastapi.concurrency import asynccontextmanager
from app.services.scheduler import start_scheduler
from app.routers import reservation, salle

@asynccontextmanager
async def startup_event(app: FastAPI):
    # Start the background scheduler
    await asyncio.create_task(start_scheduler())
    print("SCHEDULER: Scheduler started.")
    yield

app = FastAPI(
    title="G4 Integration tests",
    description="A simple Room Management WebAPI REST application",
    version="0.1.0",
    lifespan=startup_event
)

app.include_router(reservation.router)
app.include_router(salle.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SimpleWMS!"}


