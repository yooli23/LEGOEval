from util.build_helper import Component
import json


class Survey:

    def __init__(self):
        self.title = ""
        self.questions = []

    @property
    def component(self):
        return Component("Survey", title=self.title, questions=self.questions)


"""
Class for single-choice questions
"""
class RadioGroup:

    def __init__(self, name, title, choices=[], isRequired=False, colCount=1):
        self.type = "radiogroup"
        self.name = name
        self.title = title
        self.isRequired = isRequired
        self.colCount = colCount
        self.choices = choices

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


"""
Class for multiple-choices questions
"""
class CheckBox:

    def __init__(self, name, title, choices=[], hasNone=False, isRequired=False, colCount=1):
        self.type = "checkbox"
        self.name = name
        self.title = title
        self.hasNone = hasNone
        self.isRequired = isRequired
        self.colCount = colCount
        self.choices = choices

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Text:

    def __init__(self, name, title, isRequired=False, placeHolder=False, autoComplete=False):
        self.type = "text"
        self.name = name
        self.title = title
        self.isRequired = isRequired
        self.placeHolder = placeHolder
        self.autoComplete = autoComplete

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Rating:

    def __init__(self, name, title, minRateDescription="", maxRateDescription=""):
        self.type = "rating"
        self.name = name
        self.title = title
        self.minRateDescription = minRateDescription
        self.maxRateDescription = maxRateDescription

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Matrix:

    def __init__(self, name, title, columns=[], rows=[]):
        self.type = "matrix"
        self.name = name
        self.title = title
        self.columns = columns
        self.rows = rows

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Comment:

    def __init__(self, name, title):
        self.type = "comment"
        self.name = name
        self.title = title

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
