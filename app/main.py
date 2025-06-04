from fastapi import FastAPI
import uvicorn

from app.routers import article, agent, emplacement, commande, implantation, reception, mission

app = FastAPI(
    title="A simple WMS",
    description="A simple WMS REST API built with FastAPI, SQLAlchemy, and SQLite",
    version="0.1.0",
)

app.include_router(article.router)
app.include_router(agent.router)
app.include_router(emplacement.router)
app.include_router(commande.router)
app.include_router(implantation.router)
app.include_router(reception.router)
app.include_router(mission.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SimpleWMS!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)