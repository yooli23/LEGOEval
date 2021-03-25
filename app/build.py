from util.build_helper import Component, Compute
from components.page.page import Page
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk
from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.chatbot.chatbot import Chatbot
from components.compare.chats import CompareChats
from components.compare.chats_survey import CompareChatsSurvey
from components.post_chat_survey.post_chat_survey import PostChatSurvey


pipeline, compute = [], {}


TASK_TITLE = "Chat with a Chatbot"
TASK_INSTRUCTION = "In this task, you will chat with a chatbot! You will also answer a two survey questions :)"


# MTurk Support
pipeline.append(
    LoadMTurk(
        title=TASK_TITLE,
        description=TASK_INSTRUCTION,
    ).component
)


# Add a page
pipeline.append(
    Page(
        title=TASK_TITLE,
        description=TASK_INSTRUCTION,
        button="Start Task"
    )
    .component
)


pre_survey = Survey()
pre_survey.title = "Pre Survey"
pre_survey.questions = [
    RadioGroup(
        name="q1", 
        title="Have you ever talked to an AI chatbot before?", 
        choices=["Yes!", "Not sure...", "No"],
        isRequired=True
    ).toJson()
]
pipeline.append(pre_survey.component)


pipeline.append(
    Chatbot("chat",
        instruction="Please send messages until the task will end automatically. You will need to send approximately 14 messages.",
        force_human_message="Hi"
    ).component
)


post_survey = Survey()
post_survey.title = "Post Survey"
post_survey.questions = [
    RadioGroup(
        name="q2", 
        title="Did the chatbot sound 'human'?", 
        choices=["It sounded pretty close to a human!", "Not really..."],
        isRequired=True
    ).toJson()
]
pipeline.append(post_survey.component)


# Submit MTurk
pipeline.append(
    SubmitMTurk().component
)