import threading
import time
from client.client_base import ClientBase

class Subscriber(ClientBase):
    def __init__(self):
        super().__init__()
        self.latencies = []
        self.running = True

    def subscribe(self, topic):
        from common.protocol import Message
        if not topic:
            return
        self.send(Message("SUBSCRIBE", topic))

    def listen(self):
        while self.running:
            try:
                msg = self.receive()
                if not msg:
                    break

                if msg.type == "EVENT":
                    latency = time.time() - msg.timestamp
                    self.latencies.append(latency)
                    avg = sum(self.latencies) / len(self.latencies)

                    print(f"[{msg.topic}] {msg.data} | Latency: {latency:.4f}s | Avg: {avg:.4f}s")

            except Exception:
                break

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()
