import json
from faker import Faker

def handler(event, context):
    fake = Faker() # usa a biblioteca faker para gerar um nome falso aleatorio no message
    message = 'Hello {}!'.format(fake.name())  
    info = {
        "Type": "Container Example",
        "Version": 1
    }
    info_json = json.dumps(info)
    print(info_json)
    return { 
        'message' : message
    }