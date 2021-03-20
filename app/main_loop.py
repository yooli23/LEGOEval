from components.submit_mturk.submit_mturk import SubmitMTurk
from dataloader import DataLoader


# Transform our data from .txt -> list of dicts
data = [([{'id': idx, 'senderId':('bot_a' if idx % 2 == 0 else 'bot_b'), 'text': i} for idx, i in enumerate(a)], [{'id': idx, 'senderId': ('bot_a' if idx % 2 == 0 else 'bot_b'), 'text': i} for idx, i in enumerate(b)]) for a, b in [[[z for z in y.split('\n') if z != ''] for y in x.split('XXX') if y.strip() != ''] for x in "".join(open('./convo_data_example.txt', 'r').readlines()).split("---") if x.strip() != '']]


# Init our data loader
loader = DataLoader(key="CompareConvosKeyX", count=1, data=data)


def update(state, instruction):

    if instruction == 'advance':
        state.advance()

    if instruction == 'print':
        print("Printing from front end!")

    if instruction == 'request_message':        
        state.data["messages"].append({'id':len(state.data["messages"]), 'senderId':'Robot', 'text': "This is a robot...!"})
        if len(state.data["messages"]) >= 8:
            state.advance()

    if instruction == 'load_comparison':
        convo_a, convo_b = loader.pop()        
        state.data["compare_bot_a"] = convo_a        
        state.data["compare_bot_b"] = convo_b

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)
    
    return state


