# Chatbot Component

## Notes

Currently, the user is required to speak the first message for this component.

## Code

```python3
# build.py
# ...
pipeline.append(Chatbot("MyUniqueIdentiferHere").component)
```

```python3
# main_loop.py
def update(state, instruction):

    # ...

    if instruction == 'request_message':

        last_message = state.data["messages"][-1]["text"] # optionally get the last message

        state.data["messages"].append(
            {'id':len(state.data["messages"]), 
            'senderId':'Robot', 
            'text': "My custom text here"}
        ) # append a new message...

        if len(state.data["messages"]) >= 8:
            state.advance() # call advance when satisfied...
```