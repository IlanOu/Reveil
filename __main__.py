from src.base.Waker import Alarm
import sys, time, signal
from src.base.Media import *
# if __name__ == "__main__":
#     waker = Waker()
#     waker.start()



def main():
    import json 
    config = ""
    with open("./assets/store.json", 'r') as f:
        config = json.load(f)

    alarm = Alarm(config["alarms"][0])
    
    # Add wake-up actions
    # alarm.add_action({"type": "say", "params": {"message": "Bon lundi ! C'est parti pour une nouvelle semaine !"}, "delay": "00:05"})
    # alarm.add_action({"type": "say", "params": {"message": "force"}, "delay": "00:05"})
    
    # alarm.enable()
    alarm.scheduleAlarm("2024-08-09 17:03:30")


    # Keep the script running
    try:
        while True:
            time.sleep(1)
            # print("toto")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    except KeyboardInterrupt:
        print("Alarm clock stopped.")




if __name__ == "__main__":
    main()
    # from src.base.Media import MediaManager
    # MediaManager().play("https://www.youtube.com/watch?v=Pw-0pbY9JeU")