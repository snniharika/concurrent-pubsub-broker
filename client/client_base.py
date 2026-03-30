import socket
from common.utils import send_msg, recv_msg
from common.protocol import Message
from client.ssl_client import create_client_ssl

class ClientBase:
    def __init__(self, host='127.0.0.1', port=5000):
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = create_client_ssl()
        self.sock = context.wrap_socket(raw_sock, server_hostname=host)
        self.sock.connect((host, port))

    def send(self, msg):
        send_msg(self.sock, msg)

    def receive(self):
        data = recv_msg(self.sock)
        if data:
            return Message.deserialize(data)
        return None
