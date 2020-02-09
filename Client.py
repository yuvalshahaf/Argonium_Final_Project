from PlayerCharacter import PlayerCharacter
from Connection import Connection


class Client(object):
    def __init__(self, client_socket, user_id=None):
        self.user_id = user_id
        self.connection = Connection(client_socket)

        self.joined_game = False
        self.current_character_id = None
        self.characters = None


