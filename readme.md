# LEGOEval
A toolkit for dialogue system evaluation via crowdsourcing.


## Updating the front-end
- run `npm install` inside of `react_app` if you run for first time
- Remember to do `npm run build` inside of `react_app` anytime you change the front-end `js` files.


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
