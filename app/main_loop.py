from dataloader import DataLoader


def update(state, instruction):
    
    if instruction == 'request_message':    
        if len(state.data["messages"]) < 4:                          
            text = "Hello from backend!"
            new_message = {'id':len(state.data["messages"]), 'senderId':'Robot', 'text': text}
            state.data["messages"].append(new_message)
        else:
            state.advance()            

    return state


