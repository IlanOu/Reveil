# Classe Reveil simplifiée
class Reveil:
    def __init__(self):
        self.actions = []

    def add_action(self, action_func, params):
        self.actions.append((action_func, params))

    def start(self):
        for action, params in self.actions:
            action(*params)

