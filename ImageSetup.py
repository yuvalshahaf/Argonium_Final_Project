import os


def get_paths():
    paths = []
    game_folder = "FinalFinalProject"
    for path, directories, files in os.walk('C:\\'):
        if game_folder in directories:
            print(os.path.join(path, game_folder) + "\\Pictures\\")
            paths.append(os.path.join(path, game_folder) + "\\Pictures\\")
    return paths

class MapImages:
    paths = get_paths()
    DOG = []
    FIRST_MAP = []
    for path in paths:
        DOG.append(path + "Doggo-FeatureArt2-104685145.jpg")
        FIRST_MAP.append(path + "maps\\map.tmx")

class FighterImages:
    paths = get_paths()
    FIGHTER = []
    UP = []
    RIGHT = []
    DOWN = []
    LEFT = []
    for path in paths:
        FIGHTER.append(path + "fighter\\")

    for path in FIGHTER:
        for i in range(4):
            UP.append(path + "move_U\\U_" + str(i) + ".png")
            RIGHT.append(path + "move_R\\R_" + str(i) + ".png")
            DOWN.append(path + "move_D\\D_" + str(i) + ".png")
            LEFT.append(path + "move_L\\L_" + str(i) + ".png")
