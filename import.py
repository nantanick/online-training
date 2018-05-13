import json
import datetime

class userData:
    def __init__(self, file):
        data = open_json(file)

        #info
        self.name = data.get('name', None)
        self.id = data.get('id', None)
        self.personality = data.get('relation', None)
        #immediate updates
        self.problem = data.get('problem', None)
        self.location = data.get('location', None)
        self.time = datetime.datetime.now()
        self.relationData = data.get('relation', None)
        self.data = data.get('data', None)

        
    def update_immediate(self,file):
        data = open_json(file)

        #immediate updates
        self.problem = data.get('problem', None)
        self.location = data.get('location', None)
        self.time = datetime.datetime.now()
        self.relationData = data.get('relation', None)
        self.data = data.get('data', None)
        
    def update_psersonal(self,file):
        data = open_json(file)
        #info
        self.name = data.get('name', None)
        self.id = data.get('id', None)
        self.personality = data.get('relation', None)

def open_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

