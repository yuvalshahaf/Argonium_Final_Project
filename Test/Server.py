import socket


class TestServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 1729))
        self.server_socket.listen(5)

        self.connected_clients = []

class Game:

    def __init__(self):