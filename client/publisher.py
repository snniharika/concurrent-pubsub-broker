import time
from client.client_base import ClientBase
from common.protocol import Message


class Publisher(ClientBase):
    def __init__(self, host='127.0.0.1', port=5000):
        super().__init__(host, port)
        self.count = 0
        self.start_time = time.time()

    def publish(self, topic, data):
        # Basic validation
        if not topic or not data:
            print("[ERROR] Topic and data cannot be empty")
            return

        try:
            # Step 1: Create message
            msg = Message("PUBLISH", topic, data)

            # Step 2: Send message to broker
            self.send(msg)

            # Step 3: Update message count
            self.count += 1

            # Step 4: Calculate throughput
            elapsed = time.time() - self.start_time

            if elapsed > 0:
                throughput = self.count / elapsed
                print(f"Throughput: {throughput:.2f} msgs/sec")

        except Exception as e:
            print(f"[PUBLISH ERROR]: {e}")
