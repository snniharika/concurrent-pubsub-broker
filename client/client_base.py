import socket
from common.utils import send_msg, recv_msg
from common.protocol import Message
from client.ssl_client import create_client_ssl


class ClientBase:
    def __init__(self, host='127.0.0.1', port=5000):
        try:
            # Step 1: Create TCP socket
            raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Step 2: Wrap socket with SSL
            context = create_client_ssl()
            self.sock = context.wrap_socket(raw_sock, server_hostname=host)

            # Step 3: Connect to server
            self.sock.connect((host, port))

            print(f"[CONNECTED] to {host}:{port}")

        except Exception as e:
            print(f"[CONNECTION ERROR]: {e}")
            raise

    def send(self, msg):
        try:
            send_msg(self.sock, msg)
        except Exception as e:
            print(f"[SEND ERROR]: {e}")
            raise

    def receive(self):
        try:
            data = recv_msg(self.sock)
            if not data:
                return None

            return Message.deserialize(data)

        except Exception as e:
            print(f"[RECEIVE ERROR]: {e}")
            return None

    def close(self):
        try:
            self.sock.close()
            print("[DISCONNECTED]")
        except Exception:
            pass
