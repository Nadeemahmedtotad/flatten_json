from fastapi import FastAPI, HTTPException, Depends,Request,BackgroundTasks
from typing import Dict, Any

from app.utils import flatten_json
from app.auth import create_access_token
from app.schemas import LoginRequest
from app.dependencies import get_current_user
from app.tasks import check_ip
from app.telemetry import setup_telemetry
from prometheus_client import make_asgi_app

app = FastAPI(
    title="Flattened JSON Service",
    version="1.0.0"
)

# setup OpenTelemetry
setup_telemetry(app)

# expose /metrics for Prometheus/VictoriaMetrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.post("/login")
async def login(
    request: LoginRequest,
    http_request: Request,
    background_tasks: BackgroundTasks
):
    username = request.username
    client_ip = http_request.client.host

    # enqueue celery task OUTSIDE request path
    background_tasks.add_task(
        check_ip.apply_async,
        args=[username, client_ip],
        countdown=5
    )

    access_token = create_access_token(
        data={"sub": username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "ip": client_ip
    }

@app.post("/flatten")
def flatten_json_api(payload: Dict[str, Any],
                     current_user: str = Depends(get_current_user)):
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    flattened = flatten_json(payload)
    return {
        "flattened_json": flattened
    }
