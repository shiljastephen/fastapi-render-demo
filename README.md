# FastAPI + Gunicorn + Uvicorn + Docker (deployed on Render)

Gunicorn acts as the process manager, spawning several Uvicorn workers that serve the FastAPI app.

```
Client -> Render -> Gunicorn (master) -> Uvicorn worker 1 -> FastAPI
                                      -> Uvicorn worker 2 -> FastAPI
```

## Endpoints
- `GET /`        hello message
- `GET /health`  health check
- `GET /info`    worker PID, hostname, uptime (refresh to see different PIDs)
- `GET /docs`    Swagger UI

## Run locally (without Docker)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload          # dev: plain Uvicorn
gunicorn app.main:app -c gunicorn_conf.py   # prod style
```

## Run with Docker
```bash
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo
# open http://localhost:8000/info
```

## Deploy on Render (free)
1. Push this folder to a GitHub repo.
2. Go to https://dashboard.render.com -> New -> Web Service (or New -> Blueprint to use `render.yaml`).
3. Connect your repo, choose **Docker** as the runtime and the **Free** instance type.
4. Set Health Check Path to `/health`, then click Deploy.
5. Open the `https://<your-service>.onrender.com/info` URL.

Notes:
- Render sets the `PORT` env var; `gunicorn_conf.py` reads it automatically.
- Free services sleep after ~15 minutes idle, so the first request after that is slow.
