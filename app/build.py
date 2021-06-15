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

f = open('robotcry-survey-toy-v3.1_test.json',)
data = json.load(f)
dataloader = DataLoader(key="v3", count=1, data=data)
f.close()


# Define a few constants
TASK_TITLE = "Rate 15 statements taken from a conversation."
TASK_INSTRUCTION = "For this task we are trying to understand the kinds of things that are ok for a human to say, but not a machine. We will ask for your help by providing ratings on 15 statements taken from a conversation.\n\nYour responses to this HIT will be used as part of a research study. Participation in this research is completely voluntary. By accepting the HIT you consent to participate.\n\nImagine that the robot R is a friendly humanoid robot from the year 2060. R has two arms and two legs, and is capable of doing many things humans can do like riding a bike, cooking a meal, understanding complex math, and writing poetry.\n\nYou will be asked questions about responses R might make.\n\nYou must accept the HIT before continuing."
def GetCompute():
    compute = {}
    return compute

def GetPipeline():
    survey_data = dataloader.pop()
    pipeline = []
    compute = GetCompute() 
    ### ~~~ Build Your Task Below ~~~ ###
    first_page_text = survey_data["first_page_text"]
    pages_info = survey_data["pages"]
    # Instruction Page
    pipeline.append(
        Instruction(
            title=TASK_TITLE,
            description=first_page_text,
            button="Start Task"
        )
        .component
    )
    
    for page_elem in pages_info:
        page_type = page_elem["page_type"]
        if page_type == "demographics":
            questions_text = page_elem["questions"]
            questions = ConvertDemoQuestions(questions_text)
            survey = Survey("Demographic Questions")
            survey.questions = questions
            pipeline.append(survey.component)
        else:
            reminder_text = page_elem["reminder_text"]
            turn_metad = page_elem["turn_metad"]
            questions_text = page_elem["questions"]
            page_index = page_elem["page_index"]
            # Conversation Survey
            questions = ConvertQuestions(questions_text)
            messages = ConvertMessages(turn_metad)
            title = "Conversation Survey " + str(page_index)
            survey = ConversationSurvey(
                title=title, 
                questions=questions,
                paragraph=reminder_text,
                messages=messages,
                showProgressBar = "off"
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

def ConvertMessages(turn_metad):
    converted_messages = [{'id':0, 'senderId':'You', 'text': turn_metad["turn"]["turn_a"]}, {'id':1, 'senderId':'Robot R', 'text': turn_metad["turn"]["turn_b"]}]
    return converted_messages

def ConvertQuestions(questions):
    list_questions = []
    for question_elem in questions:
        if question_elem["question_type"] == "likert-5":
            list_questions.append(Rating(str(question_elem["question_id"]), question_elem["question_text"], minRateDescription = question_elem["min_description"], maxRateDescription = question_elem["max_description"], isRequired=True).toJson())
        else:
            print("ERROR in build.py")
    return list_questions

def ConvertDemoQuestions(questions):
    list_questions = []
    for question_elem in questions:
        if question_elem["question_type"] == "radio":
            list_questions.append(RadioGroup(str(question_elem["question_id"]), question_elem["question_text"], question_elem["options"], isRequired=True).toJson())
        else:
            print("ERROR in build.py")
    return list_questions
