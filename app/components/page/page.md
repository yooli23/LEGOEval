# Page Component

## Code

```python3
# build.py
# ...
start = Page()
start.title = "Hello, world!"
start.description = "These are my instructions."
start.button = "Continue"
pipeline.append(start.component)
```