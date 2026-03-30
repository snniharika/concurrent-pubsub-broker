import socket
from server.client_handler import ClientHandler
from server.topic_manager import TopicManager
from server.ssl_context import create_ssl_context

class Broker:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.topic_manager = TopicManager()
        self.context = create_ssl_context()

    def start(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((self.host, self.port))
        server_sock.listen(10)

        print(f"Secure Server running on {self.host}:{self.port}")

        while True:
            client_sock, addr = server_sock.accept()
            secure_sock = self.context.wrap_socket(client_sock, server_side=True)
            handler = ClientHandler(secure_sock, addr, self.topic_manager)
            handler.start()
