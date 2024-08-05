import json
from datetime import datetime, timedelta
from threading import Timer
from src.tools.Schelduler import Scheduler
from src.actions.ActionProtocol import ActionPermission


class Waker:
    def __init__(self):
        self.actions = []

    def add_action(self, action_func, params):
        self.actions.append((action_func, params))

    def start(self):
        for action, params in self.actions:
            action(*params)

import json
from datetime import datetime, timedelta
from threading import Timer
import pytz

class Alarm:
    def __init__(self, config):
        self.alarm_timers = {}
        self.actions = []
        self.config = self.init_config(config)
        self.enable()

    def init_config(self, config):
        # 
        actions_config = config["actions"]
        for action in actions_config:
            self.actions.append(action)
        return config
    
    def add_action(self, action_func, params):
        # TODO append ation in specific format of store (params, ...)
        self.actions.append((action_func, params))

    def trigger_alarm(self):
        print(f"Alarm triggered - id : {self.config['id']}")

        # call all Actions
        for action in self.actions:
            self.execute_action(action)

    def execute_action(self, action):
        # TODO pickle class
        action_type = action['type']
        action_type = eval(action_type)
        if (issubclass(action_type.__self__.__class__, ActionPermission)):
            # start all action if is ActionPermission 
            # TODO use delay of the action
            action["type"](action["params"])
        else:
            print(f"action does not have permission to execute - action: {action_type}")

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