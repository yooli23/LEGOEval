# Framework Name TBA
A Framework for Building Crowd Source Tasks.

## State
The `state` is a dictionary passed between the frontend, backend, and database.

It always has the following keys:
- `task_id` : The task ID representing the task
- `pipeline` : An array/list containing information about what component to currently display

The `state` does not always have the `data` key, so please check before accessing it. 

It is recommended components store temporary data in the `data` key, under another key based upon the component name, e.g `data/page`, or `data/survey`.

Thus, when you access the `state` (in python for example), you could do:

```python
state.data['data']['survey'] # Note: check these keys exist before accessing!
```
