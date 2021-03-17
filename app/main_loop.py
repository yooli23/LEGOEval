from components.submit_mturk.submit_mturk import SubmitMTurk


# Temp...
compare_bot_a_ex = [
    {'id':0, 'senderId':'bot_a', 'text': "Hello from backend!"},
    {'id':1, 'senderId':'bot_b', 'text': "This is a random message"},
    {'id':2, 'senderId':'bot_a', 'text': "Hello from backend!!!"},
    {'id':3, 'senderId':'bot_b', 'text': "another random message"},
    {'id':4, 'senderId':'bot_a', 'text': "Hello from backend!!!"},
]


def update(state, instruction):

    if instruction == 'advance':
        state.advance()

    if instruction == 'print':
        print("Printing from front end!")

    if instruction == 'request_message':        
        state.data["messages"].append({
            'id':len(state.data["messages"]), 
            'senderId':'Robot', 
            'text': "Hello from backend!"
        })
        if len(state.data["messages"]) >= 8:
            state.advance()

    if instruction == 'load_comparison':
        state.data["compare_bot_a"] = compare_bot_a_ex
        state.data["compare_bot_b"] = compare_bot_a_ex

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)
    
    return state