class ActionPermission:
    """
    Base class to define action permissions.
    """
    def __init__(self):
        pass

class RollerShutterProtocol(ActionPermission):
    """
    Class defining the methods of a roller shutter protocol.
    """
    def up(self):
        print("The up method must be implemented in the subclass.")

    def down(self):
        print("The down method must be implemented in the subclass.")

    def stop(self):
        print("The stop method must be implemented in the subclass.")

    def open_for_x_sec(self, nb_sec):
        print("The open_for_x_sec method must be implemented in the subclass.")

    def close_for_x_sec(self, nb_sec):
        print("The close_for_x_sec method must be implemented in the subclass.")

    def open_at(self, nb_sec):
        print("The open_at method must be implemented in the subclass.")



# ---------------------------------------------------------------------------- #
#                                    Example                                   #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":

    # ---------------------------------------------------------------------------- #
    #                            Create 2 Example Class                            #
    # ---------------------------------------------------------------------------- #

    class MySuperRollerShutter(RollerShutterProtocol):
        # --------- Class implementing the specific roller shutter protocol. --------- #
        def __init__(self):
            pass

        def up(self):
            print("going up")

        # Implement other methods here

    class LampThatShouldntBeHere:
        # ------------------------ Class representing a lamp. ------------------------ #
        def __init__(self):
            pass

        def on(self):
            print("led on")

    shutter = MySuperRollerShutter()
    led = LampThatShouldntBeHere()

    # --------------------- Representation of a daily action --------------------- #
    action_monday = [shutter.up, shutter.down, led.on]

    for action in action_monday:

        # ---------------------------------------------------------------------------- #
        #           IMPORTANT : Test if action have permission to be executed          #
        # ---------------------------------------------------------------------------- #
        if issubclass(action.__self__.__class__, ActionPermission):
            action()
        else:
            print("action does not have permission to execute a task")