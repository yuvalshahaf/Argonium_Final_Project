from Map import Map
from GameActions import GameActions
from Images import Images
WORLD_ID = 1


class World:
    def __init__(self):
        global WORLD_ID
        self.world_id = WORLD_ID
        WORLD_ID += 1

        self.maps = [Map(Images.MAP_TOWN)]
        self.player_characters = []

    def add_new_character(self, player_character):
        self.player_characters.append(player_character)

    def get_new_map(self, direction, current_map_location):
        directions = {
            GameActions.MAP_CHANGE_UP: self.change_map_up,
            GameActions.MAP_CHANGE_DOWN: self.change_map_down,
            GameActions.MAP_CHANGE_RIGHT: self.change_map_right,
            GameActions.MAP_CHANGE_LEFT: self.change_map_left
        }
        return directions[direction](current_map_location)

    def change_map_up(self, current_map_location):
        current_map_location[1] += 1
        for single_map in self.maps:
            if single_map.map_location == current_map_location:
                return single_map

    def change_map_down(self, current_map_location):
        current_map_location[1] -= 1
        for single_map in self.maps:
            if single_map.map_location == current_map_location:
                return single_map

    def change_map_right(self, current_map_location):
        current_map_location[0] += 1
        for single_map in self.maps:
            if single_map.map_location == current_map_location:
                return single_map

    def change_map_left(self, current_map_location):
        current_map_location[0] -= 1
        for single_map in self.maps:
            if single_map.map_location == current_map_location:
                return single_map
