import json
from pprint import pprint

from util.build_helper import Component, Compute
from components.page.page import Page as Instruction
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk
from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.chatbot.chatbot import Chatbot
from components.compare.chats import CompareChats
from components.compare.chats_survey import CompareChatsSurvey
from components.post_chat_survey.post_chat_survey import PostChatSurvey


pipeline, compute = [], {}


def branching_logic(state_data):

    # Read state data...
    should_skip = json.loads(state_data['Pre Survey'])['skip_chatbot'] == "Yes"

    # Define pages
    chat_1 = Chatbot("chat1", instruction="Please chat with the first chatbot.", force_human_message="Hi, first chatbot!").component
    page = Instruction(title="Great work!", description="You've almost finished the task!", button="Continue").component
    chat_2 = Chatbot("chat2", instruction="Please chat with the second chatbot.", force_human_message="Hi, second chatbot!").component

    # Decide what to return...
    if should_skip:
        return [chat_2]

    return [chat_1, page, chat_2]


# Update the compute dictionary
BRANCHING_KEY = "my_unique_key"
compute[BRANCHING_KEY] = branching_logic


# A few constants...
TASK_TITLE = "Chat with two Chatbots"
TASK_INSTRUCTION = "In this task, you will chat with two chatbots! Then you will answer a quick question!"


# MTurk Support
# pipeline.append(
#     LoadMTurk(
#         title=TASK_TITLE,
#         description=TASK_INSTRUCTION,
#     ).component
# )


# Instruction Page
pipeline.append(
    Instruction(
        title=TASK_TITLE,
        description=TASK_INSTRUCTION,
        button="Start Task"
    )
    .component
)


# Pre Survey
survey = Survey("pre_survey")
survey.title = "Pre Survey"
survey.questions.append(
    RadioGroup(
        "skip_chatbot", 
        "Do you want to skip the first chatbot?", 
        ["Yes", "No"]
    ).toJson()
)
pipeline.append(survey.component)


# Another Page
pipeline.append(
    Instruction(
        title="You will now start the task.",
        description="Now, you will actually talk to the chatbots...",
        button="Continue"
    )
    .component
)


"""
Option 1) Add in linear pages
"""
# pipeline.append(
#     Chatbot("chat1",
#         instruction="Please chat with the first chatbot.",
#         force_human_message="Hi, first chatbot!"
#     ).component
# )

# # Small break...
# pipeline.append(
#     Instruction(
#         title="Great work!",
#         description="You've almost finished the task!",
#         button="Continue"
#     )
#     .component
# )

# pipeline.append(
#     Chatbot("chat2",
#         instruction="Please chat with the second chatbot.",
#         force_human_message="Hi, second chatbot!"
#     ).component
# )


"""
Option 2) Branching Logic
"""
pipeline.append(Compute(BRANCHING_KEY))


# Post Survey
survey = Survey("post_survey")
survey.title = "Post Survey"
survey.questions.append(Comment("comment", "Please give feedback.").toJson())
pipeline.append(survey.component)


# Submit MTurk
# pipeline.append(
#     SubmitMTurk().component
# )