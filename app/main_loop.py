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
        if len(state.data["messages"]) >= 5:
            state.data['messages'] = []
            state.data['pause_ui'] = []
            state.advance()  
            print("advance..")
        else:
            state.data["messages"].append(
                {'id':len(state.data["messages"]), 
                'senderId':'Robot', 
                'text': query_blender([i['text'] for i in state.data["messages"]])}
            )

    if instruction == 'load_comparison':        
        """
        hi
        hi, how are you today? i just got back from a long day of work, how about you?
        That's great, I just got home from school.
        what do you do for a living? do you have any hobbies? i like to read
        ---
        hi
        hi, how are you today? i just got back from a long day of work, how about you?
        I was just painting!
        that's cool, what kind of painting do you do? i've never done anything like that before
        """
        state.data["compare_bot_a"] = [
            {'id':0, 'senderId':'bot_a', 'text': 'hi'},
            {'id':1, 'senderId':'bot_b', 'text': 'hi, how are you today? i just got back from a long day of work, how about you?'},
            {'id':2, 'senderId':'bot_a', 'text': 'That\'s great, I just got home from school.'},
            {'id':3, 'senderId':'bot_b', 'text': 'what do you do for a living? do you have any hobbies? i like to read'},
            ]
        state.data["compare_bot_b"] = [
            {'id':0, 'senderId':'bot_a', 'text': 'hi'},
            {'id':1, 'senderId':'bot_b', 'text': 'hi, how are you today? i just got back from a long day of work, how about you?'},
            {'id':2, 'senderId':'bot_a', 'text': 'I was just painting!'},
            {'id':3, 'senderId':'bot_b', 'text': 'that\'s cool, what kind of painting do you do? i\'ve never done anything like that before'},
        ]

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state


