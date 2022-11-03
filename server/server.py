from fastapi import FastAPI
from src import bound
from src import sql

app = FastAPI(
    title="Bench",
    version="0.0.0",
    swagger_ui_parameters={"displayRequestDuration": True},
)
cfg = dict()


@app.get("/run_sync")
def run_sync(cpu_test: bool = True, io_test: bool = True):
    cpu_time = bound.cpu_bound() if cpu_test else -1
    io_time = bound.io_bound(cfg["pool"]) if io_test else -1
    return dict(result=True, cpu_time=cpu_time, io_time=io_time)


@app.get("/run_async")
async def run_async(cpu_test: bool = True, io_test: bool = True):
    cpu_time = bound.cpu_bound() if cpu_test else -1
    io_time = bound.io_bound(cfg["pool"]) if io_test else -1
    return dict(result=True, cpu_time=cpu_time, io_time=io_time)


@app.get("/")
def home():
    return "Pong!"


@app.on_event("startup")
def startup():
    cfg["pool"] = sql.create_pool()


@app.on_event("shutdown")
def shutdown():
    cfg["pool"].close()
