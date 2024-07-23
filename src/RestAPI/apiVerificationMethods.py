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
    if len(data) > 0:
        for day in data:
            if day in ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]:
                pass
            else:
                return False
        return True
    else:
        return False

def add_actions_verification(data):
    if len(data) > 0:
        for currentdata in data:
            if "type" in currentdata and "params" in currentdata and "delay" in currentdata:
                pass
            else:
                return False
        return True
    else:
        return False
# ---------------------------------------------------------------------------- #
#                                  PUT METHODS                                 #
# ---------------------------------------------------------------------------- #
# For replace data
def update_name_verification(data):
    if type(data) == str:
        return True
    else:
        return False
    
def update_ringonce_verification(data):
    if type(data) == bool:
        return True
    else:
        return False

def update_isactivated_verification(data):
    if type(data) == bool:
        return True
    else:
        return False

def update_days_verification(data):
    if len(data) > 0:
        for day in data:
            if day in ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]:
                pass
            else:
                return False
        return True
    else:
        return False

def update_time_verification(data):
    if len(data) == 5:
        if data[2] == ":":
            return True
        else:
            return False 
    else:
        return False

def update_actions_verification(data):
    if len(data) > 0:
        for currentdata in data:
            if "type" in currentdata and "params" in currentdata and "delay" in currentdata:
                pass
            else:
                return False
        return True
    else:
        return False    

# ---------------------------------------------------------------------------- #
#                                DELETE METHODS                                #
# ---------------------------------------------------------------------------- #
def delete_clock_verification(data):
    return True
