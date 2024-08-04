from src.base.Waker import Waker, Alarm
import sys, time, signal

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
    alarm.add_action(print, ("Good morning!",))
    alarm.add_action(print, ("It's time to start your day!",))
    
    alarm.enable()

    # Keep the script running
    try:
        while True:
            time.sleep(1)
            print("toto")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    except KeyboardInterrupt:
        print("Alarm clock stopped.")




if __name__ == "__main__":
    main()
    # from src.base.Media import MediaManager
    # MediaManager().play("https://www.youtube.com/watch?v=Pw-0pbY9JeU")