from util.build_helper import Component

class Chatbot:

    def __init__(self, identifier, instruction="", force_human_message="Hi"):
        self.identifier = identifier
        self.instruction = instruction
        self.force_human_message = force_human_message

    @property
    def component(self):
        return Component("MyChatbot", 
            identifier=self.identifier,
            instruction=self.instruction,
            force_human_message=self.force_human_message
        )