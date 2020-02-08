import socket
import threading
from Session import Session
from Commands import Commands
from World import World
from Database import Database
import hashlib
from Connection import Connection
from Client import Client
from Images import Images

# command_info_list = [commands, info1, info2...]


class GameManager(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 1729))
        self.server_socket.listen(5)

        self.connected_clients = []
        self.sessions = []

        self.example_database = Database()

    def connect_clients(self):
        while True:
            client_socket, address = self.server_socket.accept()
            client = Client(client_socket)
            self.connected_clients.append(client)
            t = threading.Thread(target=self.communicate_client, args=(client,))
            t.start()

    def communicate_client(self, client):
        while not client.joined_game:
            command_info_list = client.connection.receive_packed()
            if command_info_list:
                command = command_info_list[0]
                command_switcher = {
                    Commands.ATTEMPT_LOGIN: self.attempt_client_login,
                    Commands.ENTER_SESSION: self.give_client_world
                }
                command_switcher[command](client, command_info_list)

    def attempt_client_login(self, client, command_info_list):
        client_connection = client.connection
        user_name = command_info_list[1]
        password = command_info_list[2]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        for user_info in self.example_database.USERS:
            if user_info[0] == user_name:
                if user_info[1] == hashed_password:
                    client_connection.send_byte(Commands.LOGIN_SUCCEEDED)
                    client_connection.send_object(user_info[2])
                else:
                    client_connection.send_byte(Commands.LOGIN_FAILED)
                    client_connection.send_packed(["Wrong password"])
                return
        client_connection.send_byte(Commands.LOGIN_FAILED)
        client_connection.send_packed(["User not found"])

    def give_client_world(self, client, command_info_list):
        #test
        requested_world_id = int(command_info_list[1])
        for session in self.sessions:
            if session.world.world_id == requested_world_id:
                session.connect_client(client)
                client.joined_game = True
                return
        for world in self.example_database.WORLDS:
            if world.world_id == requested_world_id:
                new_session = Session(world)
                new_session.connect_client(client)
                self.sessions.append(new_session)
                client.joined_game = True
                return
        msg = "World not found"
        client.connection.send_packed(msg)


def main():
    Images.load_images()
    game_manager = GameManager()
    t = threading.Thread(target=game_manager.connect_clients)
    t.start()
    input()


if __name__ == '__main__':
    main()
