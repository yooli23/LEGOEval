LoadMTurk Component

Properties:
- None currently

Instructions:
- load_mturk
    Requests the mturk dict to be like so:
        state.data['mturk'] = {
            'assignment_id':'DEFAULT RANDOM ASSIGNMENT ID, REPLACE ME!',
            'sandbox_end_point': 'https://workersandbox.mturk.com/mturk/externalSubmit',
            'production_end_point': 'https://mturk.com/mturk/externalSubmit'
        }
- advance
    Requests to advance to the next component by calling `state.advance()`
