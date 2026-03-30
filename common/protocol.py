import json
import time

class Message:
    def __init__(self, type_, topic=None, data=None):
        self.type = type_
        self.topic = topic
        self.data = data
        self.timestamp = time.time()

    def serialize(self):
        return json.dumps(self.__dict__).encode()

    @staticmethod
    def deserialize(bytes_data):
        obj = json.loads(bytes_data.decode())
        return Message(obj['type'], obj.get('topic'), obj.get('data'))
