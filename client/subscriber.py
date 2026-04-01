import threading
import time
from client.client_base import ClientBase
from common.protocol import Message


class Subscriber(ClientBase):
    def __init__(self, host='127.0.0.1', port=5000):
        super().__init__(host, port)
        self.latencies = []
        self.running = True

    def subscribe(self, topic):
        if not topic:
            print("[ERROR] Topic cannot be empty")
            return

        try:
            msg = Message("SUBSCRIBE", topic)
            self.send(msg)
            print(f"[SUBSCRIBED] {topic}")

        except Exception as e:
            print(f"[SUBSCRIBE ERROR]: {e}")

    def unsubscribe(self, topic):
        if not topic:
            print("[ERROR] Topic cannot be empty")
            return

        try:
            msg = Message("UNSUBSCRIBE", topic)
            self.send(msg)
            print(f"[UNSUBSCRIBED] {topic}")

        except Exception as e:
            print(f"[UNSUBSCRIBE ERROR]: {e}")

    def listen(self):
        while self.running:
            try:
                msg = self.receive()

                if not msg:
                    print("[DISCONNECTED FROM SERVER]")
                    break

                if msg.type == "EVENT":
                    latency = time.time() - msg.timestamp
                    self.latencies.append(latency)

                    avg = sum(self.latencies) / len(self.latencies)

                    print(f"[{msg.topic}] {msg.data} | Latency: {latency:.4f}s | Avg: {avg:.4f}s")

            except Exception as e:
                print(f"[LISTEN ERROR]: {e}")
                break

    def start(self):
        thread = threading.Thread(target=self.listen, daemon=True)
        thread.start()

    def stop(self):
        self.running = False
        self.close()
