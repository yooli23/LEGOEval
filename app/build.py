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

f = open('robotcry-survey-toy-v1.json',)
data = json.load(f)
dataloader = DataLoader(key="uniqueKeyHere", count=3, data=data)
f.close()


# Define a few constants
TASK_TITLE = "Rate 15 statements taken from a conversation."
TASK_INSTRUCTION = "For this task we are trying to understand the kinds of things that are ok for a human to say, but not a machine. We will ask for your help by providing ratings on 15 statements taken from a conversation.\n\nImagine that the robot R is a friendly humanoid robot from the year 2060. R has two arms and two legs, and is capable of doing many things humans can do like riding a bike, cooking a meal, understanding complex math, and writing poetry.\n\nYou will be asked questions about each part of a conversation."

def GetCompute():
    compute = {}
    return compute

def GetPipeline():
    survey_data = dataloader.pop()
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
    # pipeline.append(
    #     Instruction(
    #         title="TESTING",
    #         description=survey_data["pages"][0]["turn_metad"]["turn"]["turn_a"],
    #         button="Start Task"
    #     )
    #     .component
    # )
    # Chatbot Page
    # pipeline.append(
    #     Chatbot("chatbot",
    #         instruction="Please chat with the first chatbot.",
    #         force_human_message="Hi, first chatbot!"
    #     ).component
    # )

    # Conversation Survey
    survey = ConversationSurvey(
        title="Conversation Survey", 
        questions=[Comment("comment", "Please give feedback.").toJson()],
        paragraph="Testing",
        messages=[{'id':0, 'senderId':'Robot', 'text': 'Hello from backend!'}, {'id':1, 'senderId':'You', 'text': 'Hello from backend!'}, {'id':2, 'senderId':'Robot', 'text': 'Hello from backend!'}, {'id':3, 'senderId':'You', 'text': 'Hello from backend!'}]
    )
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
