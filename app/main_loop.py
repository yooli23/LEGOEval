

def update(state, instruction):       

    if instruction == 'advance':
        state.advance()

    if instruction == 'print':
        print("Printing from front end!")

    return state