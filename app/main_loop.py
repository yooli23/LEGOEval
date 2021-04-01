from components.submit_mturk.submit_mturk import SubmitMTurk


def update(state, instruction):

    if instruction == 'advance':
        state.advance() 

    if instruction == 'request_message':
        # Terminate task...
        if len(state.data["messages"]) >= 4:
            state.data['messages'] = []
            state.data['pause_ui'] = []
            state.advance()  
            print("advance..")
        else:
            # Send message from backend
            state.data["messages"].append(
                {'id':len(state.data["messages"]), 
                'senderId':'Robot', 
                'text': 'Hello from backend!'}
            )

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state


