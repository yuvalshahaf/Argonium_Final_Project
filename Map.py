import PlayerCharacter
import pygame
import pytmx


class TiledMap:
    def __init__(self, paths):
        self.path = ""
        for path in paths:
            try:
                pytmx.load_pygame(path, pixelalpha=True)
            except:
                pass
            else:
                self.path = path
                break
        self.tm = pytmx.load_pygame("Pictures/maps/map.tmx", pixelalpha=True)
        self.width = self.tm.width * self.tm.tilewidth
        self.height = self.tm.height * self.tm.tileheight

    def render(self, surface):
        ti = self.tm.get_tile_image_by_gid
        for layer in self.tm.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tm.tilewidth,
                                            y * self.tm.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface


class Map(object):
    def __init__(self, paths):
        self.paths = paths
        self.map_location = [0, 0]
        self.tiled_map = None
        self.image = None
        self.game_objects = [PlayerCharacter.FighterClass(1)]

    def initiate_map(self):
        self.tiled_map = TiledMap(self.paths)
        self.image = self.tiled_map.make_map()
