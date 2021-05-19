from util.build_helper import Component


class ConversationSurvey:

    def __init__(self, title="", questions = [], paragraph = "", messages = []):
        self.title = title
        self.questions = questions
        self.paragraph = paragraph
        self.messages = messages

    @property
    def component(self):
        return Component(
            "ConversationSurvey",         
            title=self.title,
            paragraph=self.paragraph,
            messages=self.messages,
            questions=self.questions
        )