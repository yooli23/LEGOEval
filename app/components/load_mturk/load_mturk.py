from util.build_helper import Component


class LoadMTurk:
    
    def __init__(self, title="I am a title.", description="I am a description."):
        self.title = title
        self.description = description

    @property
    def component(self):
        return Component("LoadMTurk", title=self.title, description=self.description)