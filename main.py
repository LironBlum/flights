import logging
from fastapi import FastAPI
from app.flight_controller import router as flight_router
from app.flight_service import load_flights, update_flights
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
app.include_router(flight_router, prefix="/flight", tags=["Flight"])
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_flights()

logger.info("Starting scheduler")
scheduler = BackgroundScheduler()
scheduler.start()


def daily_flight_status_update():
    update_flights()


scheduler.add_job(daily_flight_status_update, "cron", hour=0, minute=0)


## use this hack to run daily_flight_status_update on serverr startup
@app.on_event("startup")
def startup_event():
    daily_flight_status_update()


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
