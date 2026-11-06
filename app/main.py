import os
import socket
import time

from fastapi import FastAPI

app = FastAPI(title="Uvicorn + Gunicorn + Docker Demo")
START_TIME = time.time()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI running on Gunicorn + Uvicorn in Docker!"}


@app.get("/health")
async def health():
    # Used by Render as the health check endpoint
    return {"status": "ok"}


@app.get("/info")
async def info():
    # Refresh this endpoint several times: the PID changes when a different
    # Gunicorn worker handles the request, which shows multiple workers at work.
    return {
        "worker_pid": os.getpid(),
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - START_TIME, 1),
        "port": os.getenv("PORT", "8000"),
    }
