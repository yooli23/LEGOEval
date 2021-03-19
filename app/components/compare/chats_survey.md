# Compare Chats with a Survey

## Notes

- See the `survey` component for more details about how to construct a survey for your task.

## Code

```python3
# build.py

from components.compare.chats import CompareChatsSurvey

# ...

survey = CompareChatsSurvey("RandomComparison", text="My instructions here for the survey!")

survey.title = "Unique Survey Name here..."

text1 = Text("name", "What is your name?")
survey.questions.append(text1.toJson())

pipeline.append(survey.component)
```

```python3
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()

    if instruction == 'load_comparison':
        # Loads two conversations, and will display them side by side
        state.data["compare_bot_a"] = [{'id': 0, 'senderId': 'bot_a', 'text':"Hey how are you?"}, {'id': 1, 'senderId': 'bot_a', 'text':"Great thanks!"}]
        state.data["compare_bot_b"] = [{'id': 0, 'senderId': 'bot_b', 'text':"How's it going?"}]
```