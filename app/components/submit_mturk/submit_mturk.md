# Load MTurk

## Notes

- Please place this as the **last** component at the start of your pipline.
- Please only add this component when running `launch_hits.py`, otherwise, comment it out.

## Code

```python3
# build.py
# ...
submit = SubmitMTurk()
pipeline.append(submit.component)
```

```python3
# main_loop.py
from components.submit_mturk.submit_mturk import SubmitMTurk

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()

    # ...

    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)
```