# ---------------------------------------------------------------------------- #
#                                 POST METHODS                                 #
# ---------------------------------------------------------------------------- #
# For add data
def add_alarm_verification(data):
    if "name" in data and "ringOnce" in data and "alreadyRingOnce" in data and "isActivated" in data and "days" in data and "time" in data and "actions" in data:
        return True
    else:
        return False

def add_days_verification(data):
    days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    if data in days:
        return True
    else:
        return False

def add_actions_verification(data):
    return True
# ---------------------------------------------------------------------------- #
#                                  PUT METHODS                                 #
# ---------------------------------------------------------------------------- #
# For replace data
def update_name_verification(data):
    return True

def update_ringonce_verification(data):
    return True

def update_isactivated_verification(data):
    return True

def update_days_verification(data):
    return True

def update_time_verification(data):
    return True

def update_actions_verification(data):
    return True

# ---------------------------------------------------------------------------- #
#                                DELETE METHODS                                #
# ---------------------------------------------------------------------------- #
def delete_clock_verification(data):
    return True
