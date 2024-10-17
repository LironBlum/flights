import logging
from fastapi import FastAPI
from app.flight_controller import router as flight_router
from app.flight_service import load_flights, update_flights
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
app.include_router(flight_router, prefix="/flight", tags=["Flight"])
logger = logging.getLogger(__name__)

logger.info("Loading flights data from csv file to memory")
load_flights()

logger.info("Starting scheduler")
scheduler = BackgroundScheduler()
scheduler.start()


# Daily scheduled task
def daily_flight_status_update():
    ##TODO add try except block
    logger.info("Updating daily flights status")
    update_flights()
    logger.info("Daily flights status updated")


## scheduled job to run daily
scheduler.add_job(daily_flight_status_update, "cron", hour=0, minute=0)


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
