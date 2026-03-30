from client.client_base import ClientBase
from common.protocol import Message

class Publisher(ClientBase):
    def publish(self, topic, data):
        self.send(Message("PUBLISH", topic, data))
