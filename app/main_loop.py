from components.submit_mturk.submit_mturk import SubmitMTurk
from load_meena_blender_pairs import load as load_pairs
from dataloader import DataLoader


loader = DataLoader(key="BlenderMeena8", count=1, data=load_pairs(count=50))


def update(state, instruction):  

    if instruction == 'advance':
        state.advance() 

    if instruction == 'load_comparison':
        """Meena is left, Blender is right"""
        state.data["compare_bot_a"], state.data["compare_bot_b"] = loader.pop()         
     
    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state


