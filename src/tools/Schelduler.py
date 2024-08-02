from apscheduler.schedulers.background import BackgroundScheduler
from src.tools.Singleton import singleton

@singleton
class Scheduler():

    def __init__(self) -> None:
        self.scheduler = BackgroundScheduler()
    
    def scheduleTask(self, taskAction, date):
        #TODO test date format
        self.scheduler.add_job(taskAction, 'date', run_date=date)#'2024-08-03 12:00:00')

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
