import json

from util.build_helper import Component, Compute
from components.page.page import Page as Instruction
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk
from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.chatbot.chatbot import Chatbot
from components.compare.chats import CompareChats
from components.compare.chats_survey import CompareChatsSurvey
from components.post_chat_survey.post_chat_survey import PostChatSurvey
from components.conversation_survey.conversation_survey import ConversationSurvey
from dataloader import DataLoader

# Define a few constants
TASK_TITLE = "Chat with a chatbot!"
TASK_INSTRUCTION = "In this task, you will chat with a chatbot! Then you will answer a quick question!"

def GetCompute():
    compute = {}
    return compute

def GetPipeline():
    pipeline = []
    compute = GetCompute() 
    ### ~~~ Build Your Task Below ~~~ ###
    # Instruction Page
    pipeline.append(
        Instruction(
            title=TASK_TITLE,
            description=TASK_INSTRUCTION,
            button="Start Task"
        )
        .component
    )

    # Chatbot Page
    pipeline.append(
        Chatbot("chatbot",
            instruction="Please chat with the first chatbot.",
            force_human_message="Hi, first chatbot!"
        ).component
    )

    # Post Survey
    survey = Survey("post_survey")
    survey.title = "Post Survey"
    survey.questions.append(Comment("comment", "Please give feedback.").toJson())
    pipeline.append(survey.component)

    ### ~~~ End of Your Task ~~~ ###
    return pipeline

def GetMturkPipeline():
    mturk_pipeline = []
    mturk_pipeline = GetPipeline()
    # MTurk Support
    mturk_pipeline.insert(0,
        LoadMTurk(
            title=TASK_TITLE,
            description=TASK_INSTRUCTION,
        ).component
    )

    # Submit MTurk
    mturk_pipeline.append(
        SubmitMTurk().component
    )
    return mturk_pipeline