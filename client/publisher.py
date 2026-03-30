import time
from client.client_base import ClientBase
from common.protocol import Message

class Publisher(ClientBase):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.start_time = time.time()

    def publish(self, topic, data):
        if not topic or not data:
            return

        try:
            self.send(Message("PUBLISH", topic, data))
            self.count += 1

            elapsed = time.time() - self.start_time
            if elapsed > 0:
                throughput = self.count / elapsed
                print(f"Throughput: {throughput:.2f} msgs/sec")

        except Exception as e:
            print(f"Publish failed: {e}")
