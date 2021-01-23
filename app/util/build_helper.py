class Component:

    def __init__(self, name, **data):
        self.name = name
        self.data = dict(data)

    def encode(self):
        res = {
            'class': 'Component',
            'name': self.name,
            'data': self.data
        }
        return res


class Compute:

    def __init__(self, name):
        self.name = name

    def encode(self):
        res = {
            'class': 'Compute',
            'name': self.name            
        }
        return res


class PipelineHelper:

    @staticmethod
    def encode(pipeline):
        return [x.encode() for x in pipeline]

    @staticmethod
    def decode(data):
        pipeline = []             
        for i in data:
            if i['class'] == 'Compute':
                pipeline.append(Compute(name=i['name']))
            elif i['class'] == 'Component':
                pipeline.append(Component(name=i['name'], **i['data']))
        return pipeline