from apscheduler.schedulers.background import BackgroundScheduler
from app.services.availability import update_room_availability

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_room_availability, 'interval', minutes=1)
    scheduler.start()
    print("Scheduler started. Press Ctrl+C to stop.")

    try:
        # Garde le processus vivant
        import time
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
