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


TASK_TITLE = "Chat with two Chatbots"
TASK_INSTRUCTION = "In this task, you will chat with two chatbots! Then you will answer a quick question!"


f = lambda state: Instruction(title="Page A") if state['Post Survey']['long_conversation'] == 'Yes' \
                  else Instruction(title="Page B")

key = "my_branching_logic"

compute[key] = f

pipeline.append(Compute(key).component)


# MTurk Support
# pipeline.append(
#     LoadMTurk(
#         title=TASK_TITLE,
#         description=TASK_INSTRUCTION,
#     ).component
# )


# Add a page
pipeline.append(
    Instruction(
        title=TASK_TITLE,
        description=TASK_INSTRUCTION,
        button="Start Task"
    )
    .component
)

survey = Survey("Test")
survey.title = "Post Survey"
survey.questions.append(
    RadioGroup(
        "long_conversation", 
        "Did the speaker sound like a human?", 
        ["Yes", "No"]
    ).toJson()
)
survey.questions.append(Comment("comment", "Please give feedback.").toJson())
pipeline.append(survey.component)


pipeline.append(
    Chatbot("chat1",
        instruction="Please chat with the first chatbot.",
        force_human_message="Hi"
    ).component
)

pipeline.append(
    Instruction(
        title="Break!",
        description="You'll now chat with second bot!",
        button="Continue"
    )
    .component
)


pipeline.append(
    Chatbot("chat2",
        instruction="Please chat with the second chatbot.",
        force_human_message="Hi"
    ).component
)

# survey = CompareChatsSurvey("CompareChats", text="Please compare these two conversations below.")
# survey.title = "Compare Chats"
# survey.questions.append(
#     RadioGroup(
#         "long_conversation", 
#         "Which conversation did you enjoy more?", 
#         ["LEFT Conversation", "RIGHT Conversation"]
#     ).toJson()
# )
# survey.questions.append(Comment("comment", "Please give feedback.").toJson())
# pipeline.append(survey.component)


"""
multiple chatbots on one screen

component = MultiChatBot()

component.add_group(
    Vertical(
        Chatbot1(color="0x12938"), Chatbot2()
    )
)

Chatbot1 
Chabot2
"""


# Submit MTurk
# pipeline.append(
#     SubmitMTurk().component
# )