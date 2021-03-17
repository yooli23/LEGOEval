from util.build_helper import Component


class CompareChats:

    def __init__(self, identifier, text="Choose the conversation that you prefer!", chat_bot_a_title="bot_a", chat_bot_b_title="bot_b"):
        self.identifier = identifier
        self.text = text
        self.bot_a = chat_bot_a_title
        self.bot_b = chat_bot_b_title

    @property
    def component(self):
        return Component(
            "CompareChats", 
            identifier=self.identifier,
            text=self.text,
            chatbotA=self.bot_a,
            chatbotB=self.bot_b,
        )