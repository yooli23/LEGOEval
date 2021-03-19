# Compare Chats

## Notes

- Use this component **DIRECTLY** after the `chatbot` component.
- See the `survey` component for more details about how to construct a survey for your task.
- See the `chatbot` component to see what details you need to include for the `main_loop.py`

## Code

```python3
# build.py

from components.compare.chats import CompareChats

# ...

pipeline.append(CompareChats(identifier="UniqueIdentifierHere").component)
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