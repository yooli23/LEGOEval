from util.build_helper import Component


class RandomExample:

    def __init__(self,  button = "Print!"):        
        if button is not None:
            self.button = button
        else:
            self.button = "Print!"

    @property
    def component(self):
        return Component("RandomExample", button_name=self.button)
