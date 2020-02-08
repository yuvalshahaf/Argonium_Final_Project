from World import World
from PlayerCharacter import PlayerCharacter

# TODO: create an actual database
class Database(object):
    def __init__(self):
        self.USERS = [
            ("yuval", "adcaec3805aa912c0d0b14a81bedb6ff", [0, 1]),  # 23456
            ("ooga", "827ccb0eea8a706c4c34a16891f84e7b", [0, 0]),  # 12345
        ]

        self.WORLDS = [
            World(),
            World(),
            World(),
        ]
