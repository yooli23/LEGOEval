from util.build_helper import Component, Compute
from components.page.page import Page
from components.random_example.random_example import RandomExample


compute = {}

pipeline = []


start = Page()
start.title = "Hello, world!"
start.description = "These are my instructions."
start.button = "Continue"
pipeline.append(start.component) 

end = Page()
end.title = "Finished Task"
end.description = "You completed the task!"
end.button = "Done"
pipeline.append(end.component)

test = RandomExample("Click me to print!")
pipeline.append(test.component)