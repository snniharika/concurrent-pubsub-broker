import threading
from client.client_base import ClientBase
from common.protocol import Message

class Subscriber(ClientBase):
    def subscribe(self, topic):
        self.send(Message("SUBSCRIBE", topic))

    def listen(self):
        while True:
            msg = self.receive()
            if msg and msg.type == "EVENT":
                print(f"[{msg.topic}] {msg.data}")

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()
