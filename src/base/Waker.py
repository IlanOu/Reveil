import json
from datetime import datetime, timedelta
from threading import Timer

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
    def __init__(self, config_file='assets/alarm_config.json'):
        self.config_file = config_file
        self.config = self.load_config()
        self.alarm_timers = {}
        self.action_handlers = {}

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Config file not found. Using default configuration.")
            return {"alarms": [], "settings": {"timezone": "Europe/Paris", "24h_format": True}}

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def schedule_alarms(self):
        for alarm in self.config['alarms']:
            self.schedule_alarm(alarm)

    def schedule_alarm(self, alarm):
        now = datetime.now(pytz.timezone(self.config['settings']['timezone']))
        alarm_time = datetime.strptime(alarm['time'], "%H:%M").time()
        alarm_day = alarm['day']
        
        days_ahead = self.days_until(alarm_day)
        alarm_datetime = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)
        alarm_datetime += timedelta(days=days_ahead)

        delay = (alarm_datetime - now).total_seconds()
        self.alarm_timers[alarm_day] = Timer(delay, self.trigger_alarm, [alarm])
        self.alarm_timers[alarm_day].start()

        print(f"Alarm scheduled for {alarm_day} at {alarm_time}")

    def trigger_alarm(self, alarm):
        print(f"Alarm triggered for {alarm['day']} at {alarm['time']}")
        for action in alarm['actions']:
            self.execute_action(action)
        self.schedule_alarm(alarm)  # Reschedule for next week

    def execute_action(self, action):
        action_type = action['type']
        if action_type in self.action_handlers:
            self.action_handlers[action_type](action['params'])
        else:
            print(f"Unknown action type: {action_type}")

    def days_until(self, day):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        today = datetime.now(pytz.timezone(self.config['settings']['timezone'])).weekday()
        target = days.index(day)
        return (target - today) % 7

    def run(self):
        self.schedule_alarms()

    def stop(self):
        for timer in self.alarm_timers.values():
            timer.cancel()
        print("All alarms stopped.")

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

