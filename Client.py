from PlayerCharacter import PlayerCharacter
from Connection import Connection


class Client(object):
    def __init__(self, client_socket):
        self.connection = Connection(client_socket)

        self.joined_game = False
        self.current_character = None
        self.characters = None


