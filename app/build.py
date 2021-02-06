from util.build_helper import Component, Compute
from components.page.page import Page
from components.random_example.random_example import RandomExample
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk


compute = {}

pipeline = []


load = LoadMTurk()
pipeline.append(load.component)

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

submit = SubmitMTurk()
pipeline.append(submit.component)