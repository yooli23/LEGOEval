from util.build_helper import Component


class ConversationSurvey:

    def __init__(self, title="", questions = [], paragraph = "", messages = [], showProgressBar = "top"):
        self.title = title
        self.questions = questions
        self.paragraph = paragraph
        self.messages = messages
        self.showProgressBar = showProgressBar

    @property
    def component(self):
        return Component(
            "ConversationSurvey",         
            title=self.title,
            paragraph=self.paragraph,
            messages=self.messages,
            questions=self.questions,
            showProgressBar=self.showProgressBar
        )