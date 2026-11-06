import multiprocessing
import os

# Render injects PORT; default to 8000 locally
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"

# Gunicorn is the process manager; each worker runs Uvicorn (ASGI server)
worker_class = "uvicorn_worker.UvicornWorker"

# Render's free tier has 0.1 CPU / 512 MB RAM, so keep workers low.
# Override with the WEB_CONCURRENCY env var if you like.
workers = int(os.getenv("WEB_CONCURRENCY", min(2, multiprocessing.cpu_count() * 2 + 1)))

timeout = 60
graceful_timeout = 30
keepalive = 5

accesslog = "-"   # log to stdout
errorlog = "-"
loglevel = "info"
