# Post-chat Survey

## Notes

- Use this component **DIRECTLY** after the `chatbot` component.
- See the `survey` component for more details about how to construct a survey for your task.
- See the `chatbot` component to see what details you need to include for the `main_loop.py`

## Code

```python3
# build.py

from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.post_chat_survey.post_chat_survey import PostChatSurvey

# ...

pipeline.append(Chatbot("Chat1").component)
pipeline.append(PostChatSurvey(title="A post chat survey", questions=[Text("overall", "How was the chatbot experience, overall?").toJson()]).component)
```

```python3
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()
```