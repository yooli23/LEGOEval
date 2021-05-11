from components.submit_mturk.submit_mturk import SubmitMTurk

# Import dataloader
from dataloader import DataLoader

# Load data form folder
# [ONE_CONVO, TWO_CONVO, THREE_CONVO] from a text file
ONE_CONVO = [{'id':0, 'senderId':'Robot', 'text': 'Hello from backend!'}, {'id':1, 'senderId':'You', 'text': 'Hello from backend!'}, {'id':2, 'senderId':'Robot', 'text': 'Hello from backend!'}, {'id':3, 'senderId':'You', 'text': 'Hello from backend!'}]
your_formatted_convo_from_file = [('key1', ONE_CONVO), ('key2', ONE_CONVO)]

# Create dataloader
dataloader = DataLoader(key="uniqueKeyHere", count=3, data=your_formatted_convo_from_file)

def update(state, instruction):

    # Advance to a new page
    if instruction == 'advance':
        state.advance() 

    if instruction == 'load_single_conversation':
        # Put 'You' for senderId, else, put anything :)

        # Here is asking for one conversation        
        key, convo = dataloader.pop()
        state.data["convo_key"] = key
        state.data["messages"] = convo
        state.data["paragraph"] = "Hello, I am a paragraph!!!!"

    if instruction == 'request_message':
        # Terminate task...
        if len(state.data["messages"]) >= 4:            
            state.advance()            
        else:
            # Send message from backend
            state.data["messages"].append(
                {'id':len(state.data["messages"]), 
                'senderId':'Robot', 
                'text': 'Hello from backend!'}
            )

    # Submit MTurk if necesscary
    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state


