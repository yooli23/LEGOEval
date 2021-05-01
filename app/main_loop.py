from components.submit_mturk.submit_mturk import SubmitMTurk


def update(state, instruction):

    # Advance to a new page
    if instruction == 'advance':
        state.advance() 

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


