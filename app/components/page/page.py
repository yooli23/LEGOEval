from util.build_helper import Component


class Page:

    def __init__(self, title="I am a title.", description="I am a description.", button="Continue"):
        self.title = title
        self.description = description
        self.button = button

    @property
    def component(self):
        return Component("Page", title=self.title, description=self.description, button_name=self.button)