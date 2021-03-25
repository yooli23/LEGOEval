import requests

from components.submit_mturk.submit_mturk import SubmitMTurk


def query_blender(history):
    url = "https://chilly-dragon-13.loca.lt"
    url += '/blender'
    response = requests.post(url, json={'history': history})    
    return response.json()['result']


def update(state, instruction):

    if instruction == 'advance':
        state.advance() 

    if instruction == 'request_message':
        if len(state.data["messages"]) >= (13 * 2):
            state.advance()  
        else:
            state.data["messages"].append(
                {'id':len(state.data["messages"]), 
                'senderId':'Robot', 
                'text': query_blender([i['text'] for i in state.data["messages"]])}
            )

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state


