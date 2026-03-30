import threading
from common.protocol import Message
from common.utils import recv_msg, send_msg

class ClientHandler(threading.Thread):
    def __init__(self, sock, addr, topic_manager):
        super().__init__()
        self.sock = sock
        self.addr = addr
        self.topic_manager = topic_manager
        self.running = True

    def run(self):
        print(f"[CONNECTED] {self.addr}")
        try:
            while self.running:
                data = recv_msg(self.sock)
                if not data:
                    break

                msg = Message.deserialize(data)
                self.handle_message(msg)
        except Exception as e:
            print(f"[ERROR] {self.addr}: {e}")
        finally:
            self.cleanup()

    def handle_message(self, msg):
        if msg.type == "SUBSCRIBE":
            self.topic_manager.subscribe(msg.topic, self)

        elif msg.type == "UNSUBSCRIBE":
            self.topic_manager.unsubscribe(msg.topic, self)

        elif msg.type == "PUBLISH":
            subscribers = self.topic_manager.get_subscribers(msg.topic)
            for sub in subscribers:
                try:
                    send_msg(sub.sock, Message("EVENT", msg.topic, msg.data))
                except:
                    pass

    def cleanup(self):
        print(f"[DISCONNECTED] {self.addr}")
        self.sock.close()
