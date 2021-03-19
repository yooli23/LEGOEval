# Load MTurk

## Notes

- Please place this as the first component at the start of your pipline.
- Please only add this component when running `launch_hits.py`, otherwise, comment it out.

## Code

```python3
# build.py
# ...
load = LoadMTurk()
pipeline.append(load.component)
```

```python3
# main_loop.py
def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()
```