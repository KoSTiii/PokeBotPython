

class Action(object):
    """
    Base Action class for handling actions
    """

    def __init__(self, pokebot):
        self.pokebot = pokebot
        self.data_manager = pokebot.data_manager

    def make_action(self):
        pass


class FortPokestopAction(Action):
    """
    Action for spining the pokestop
    """

    def __init__(self, pokebot):
        Action.__init__(self, pokebot)
