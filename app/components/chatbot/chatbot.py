from util.build_helper import Component

class Chatbot:

    def __init__(self, identifier):
        self.identifier = identifier

    @property
    def component(self):
        return Component("MyChatbot", identifier=self.identifier)