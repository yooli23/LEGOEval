from util.build_helper import Component


class CompareChatsSurvey:

    def __init__(self, identifier, title="", questions = [], text="", chat_bot_a_title="bot_a", chat_bot_b_title="bot_b"):
        self.title = title
        self.questions = questions
        self.identifier = identifier
        self.text = text
        self.bot_a = chat_bot_a_title
        self.bot_b = chat_bot_b_title

    @property
    def component(self):
        return Component(
            "CompareChatsSurvey", 
            identifier=self.identifier,
            text=self.text,
            chatbotA=self.bot_a,
            chatbotB=self.bot_b,
            title=self.title, 
            questions=self.questions
        )