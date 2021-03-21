# Page Component

## Code

```python3
# build.py
from components.page.page import Page

# ...

start = Page()
start.title = "Hello, world!"
start.description = "These are my instructions."
start.button = "Continue"
pipeline.append(start.component)
```

```python3
# main_loop.py

# ...

def update(state, instruction):    
    
    # ...

    if instruction == 'advance':
        state.advance()

    return state 
```