from Map import Map
from GameActions import GameActions
from Images import Images
import PlayerCharacter


class World:
    WORLD_ID = 0
    def __init__(self):
        self.world_id = World.WORLD_ID
        World.WORLD_ID += 1

        self.maps = [Map(Images.MAP_TOWN)]
        self.player_characters = [PlayerCharacter.FighterClass(1)]

    def add_new_character(self, player_character):
        self.player_characters.append(player_character)