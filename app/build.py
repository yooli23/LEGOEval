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


# MTurk Support
pipeline.append(
    LoadMTurk().component
)


# Add a page
pipeline.append(
    Page(
        title="Compare Two Conversations",
        description="In this task, you will compare two conversations, and answer a few brief questions about them.",
        button="Start Task"
    )
    .component
)


# Compare chats
survey = CompareChatsSurvey("CompareChats", text="Please compare these two conversations below.")
survey.title = "Compare Chats"
survey.questions.append(
    RadioGroup(
        "long_conversation", 
        "Who would you prefer to talk to for a long conversation?", 
        ["LEFT Conversation", "RIGHT Conversation"]
    ).toJson()
)
survey.questions.append(
    RadioGroup(
        "human", 
        "Which speaker sounds more human?", 
        ["LEFT Conversation", "RIGHT Conversation"]
    ).toJson()
)
survey.questions.append(Comment("feedback", "Please provide a brief justification for your choice (In a few words)").toJson())
pipeline.append(survey.component)


pipeline.append(
    SubmitMTurk().component
)