import os
import json
from random import shuffle


def load_meena():
    data = []
    with open('./meena.txt', 'r') as f:
        convo = []
        for line in f.readlines():
            if line != "\n":
                convo.append(line.split(":")[-1])
            else:
                data.append(convo[1:])
                convo = []
    return data


def load_blender():
    data = []
    with open('./blender.txt', 'r') as f:                
        for line in f.readlines():
            convo = []
            for x in [(x[0]['text'].split(":")[-1], x[1]['text']) for x in json.loads(line)['dialog'][1:]]:        
                convo.append(x[0])
                convo.append(x[1])
            data.append(convo)
    return data


def convert_data(data, max_turns=15):
    final = []
    for convo in data:
        result = []
        for idx, message in enumerate(convo[:max_turns]):
            result.append({'id': idx, 'senderId': ('bot_a' if idx % 2 == 0 else 'bot_b'), 'text': message})
        final.append(result)
    return final


def load(count=100):
    a = convert_data(load_meena())[:count]
    b = convert_data(load_blender())[:count]
    shuffle(a)
    shuffle(b)
    return list(zip(a, b))[:count]


if __name__=='__main__':
    x = load()
    a, b = x.pop()
    print(b[0])