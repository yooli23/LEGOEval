from util.build_helper import Component, Compute
from components.page.page import Page
from components.random_example.random_example import RandomExample
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk
from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.chatbot.chatbot import Chatbot
from components.compare.chats import CompareChats


compute = {}

pipeline = []


# Load MTurk
# load = LoadMTurk()
# pipeline.append(load.component)

# Page
start = Page()
start.title = "Hello, world!"
start.description = "These are my instructions."
start.button = "Continue"
pipeline.append(start.component) 

# Compare Chats Example
pipeline.append(CompareChats("Comparison1").component)

pipeline.append(CompareChats("Comparison2", text="Please select your preferred chat one more time!").component)

# Chatbot
# chatbot = Chatbot(identifier="chatbot_1")
# pipeline.append(chatbot.component)

# Survey
# survey = Survey()
# survey.title = "Task Survey"
# text1 = Text("name", "What is your name?")
# survey.questions.append(text1.toJson())
# radioGroup1 = RadioGroup("major", "What is your major?", ["Computer Science", "Biology", "Philosophy", "Art History"])
# survey.questions.append(radioGroup1.toJson())
# checkBox1 = CheckBox("majors", "What are your majors?",
#                      ["Computer Science", "Biology", "Philosophy", "Art History", "Music"], True)
# survey.questions.append(checkBox1.toJson())
# rating1 = Rating("food", "How would you rate the food at the school cafeteria?", "Horrible", "Fantastic")
# survey.questions.append(rating1.toJson())
# matrix1 = Matrix("moreOnFood", "How would you rate the food at the school cafeteria (in detail)?")
# matrix1.columns = [{"value": 1, "text": "bad"},
#                     {"value": 2, "text": "alright"},
#                     {"value": 3, "text": "good"}]
# matrix1.rows = [{"value": "appearance", "text": "food appearance"},
#                     {"value": "taste", "text": "food taste"},
#                     {"value": "price", "text": "food price"}]
# survey.questions.append(matrix1.toJson())
# comment1 = Comment("feedback", "Any advice to help us improve?")
# survey.questions.append(comment1.toJson())
# pipeline.append(survey.component)

# Page
end = Page()
end.title = "Finished Task"
end.description = "You completed the task!"
end.button = "Done"
pipeline.append(end.component)

# Submit MTurk
# submit = SubmitMTurk()
# pipeline.append(submit.component)