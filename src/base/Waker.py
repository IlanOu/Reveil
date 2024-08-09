import json
from datetime import datetime, timedelta
from threading import Timer
from src.tools.Schelduler import Scheduler
from src.actions.ActionProtocol import ActionPermission
from src.base.Media import MediaManager

class ActionManager:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def execute_action(self):

        # call all Actions
        for action in self.actions:

            action_type = action['type']
            # TODO use delay of the action
            # TODO test if class is herited from action permission
            match(action_type):
                case "play":
                    MediaManager().play(action["params"]["music_url"])
                case "volet":
                    pass
                case "lamp":
                    pass
                case "print":
                    print(action["params"]["message"])

            # if (issubclass(action_type.__self__.__class__, ActionPermission)):
            #     # start all action if is ActionPermission 
            #     action["type"](action["params"])
            # else:
            #     print(f"action does not have permission to execute - action: {action_type}")

import json
from datetime import datetime, timedelta
from threading import Timer
import pytz

class Alarm:
    def __init__(self, config):
        self.alarm_timers = {}
        self.actionManager = ActionManager()
        self.config = self.init_config(config)
        self.enable()

    def init_config(self, config):
        # feed action of the config file
        actions_config = config["actions"]
        for action in actions_config:
            self.actionManager.add_action(action)
        return config
    
    def add_action(self, action):
        self.actionManager.add_action(action)

    def trigger_alarm(self):
        print(f"Alarm triggered - id : {self.config['id']}")

        self.actionManager.execute_action()

    def enable(self):
        Scheduler().start() # start Scheduler 

    def disable(self):
        Scheduler().stop() # start Scheduler 

    def scheduleAlarm(self, date):
        Scheduler().scheduleTask(self.trigger_alarm, date)



class Alarm_manager():

    def __init__(self, alarms) -> None:
        self.alarms = alarms   
    

# Usage
if __name__ == "__main__":
    alarm = Alarm()
    alarm.run()

    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopping alarms...")
        alarm.stop()
        print("Program terminated.")



# ---------------------------------------------------------------------------- #
#                                  TOOLS save                                  #
# ---------------------------------------------------------------------------- #
def days_until(config, day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.now(pytz.timezone(config['settings']['timezone'])).weekday()
    target = days.index(day)
    return (target - today) % 7

# def schedule_alarms(self):
#         for alarm in self.config['alarms']:
#             self.schedule_alarm(alarm)

#     def schedule_alarm(self, alarm):
#         now = datetime.now(pytz.timezone(self.config['settings']['timezone']))
#         alarm_time = datetime.strptime(alarm['time'], "%H:%M").time()
#         alarm_day = alarm['day']
        
#         days_ahead = self.days_until(alarm_day)
#         alarm_datetime = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)
#         alarm_datetime += timedelta(days=days_ahead)

#         delay = (alarm_datetime - now).total_seconds()
#         self.alarm_timers[alarm_day] = Timer(delay, self.trigger_alarm, [alarm])
#         self.alarm_timers[alarm_day].start()

#         print(f"Alarm scheduled for {alarm_day} at {alarm_time}")