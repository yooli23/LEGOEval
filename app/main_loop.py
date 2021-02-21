from components.submit_mturk.submit_mturk import SubmitMTurk

def update(state, instruction):

    if instruction == 'advance':
        state.advance()

    if instruction == 'print':
        print("Printing from front end!")

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state) #untested if this succeeds in marking db files as complete
    
    return state