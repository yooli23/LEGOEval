from util.build_helper import Component


class ConversationSurvey:

    def __init__(self, title="", questions = []):
        self.title = title
        self.questions = questions

    @property
    def component(self):
        return Component(
            "ConversationSurvey",            
            title=self.title, 
            questions=self.questions
        )