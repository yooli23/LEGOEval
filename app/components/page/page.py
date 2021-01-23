from util.build_helper import Component


class Page:

    def __init__(self):
        self.title = "I am a title."
        self.description = "I am a description."
        self.button = "Continue"

    @property
    def component(self):
        return Component("Page", title=self.title, description=self.description, button_name=self.button)
