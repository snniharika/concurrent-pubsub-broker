from collections import defaultdict
import threading

class TopicManager:
    def __init__(self):
        self.topics = defaultdict(set)
        self.lock = threading.Lock()

    def subscribe(self, topic, client):
        with self.lock:
            self.topics[topic].add(client)

    def unsubscribe(self, topic, client):
        with self.lock:
            self.topics[topic].discard(client)

    def get_subscribers(self, topic):
        with self.lock:
            return list(self.topics[topic])
