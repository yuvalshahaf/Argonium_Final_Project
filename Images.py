import os


class Images:
    PATHS = []

    FIGHTER_PATHS = []
    FIGHTER_MOVE_UP_IMAGES = []
    FIGHTER_MOVE_DOWN_IMAGES = []
    FIGHTER_MOVE_RIGHT_IMAGES = []
    FIGHTER_MOVE_LEFT_IMAGES = []

    MAPS_PATHS = []
    MAP_TOWN_PATHS = []

    @staticmethod
    def load_images():
        game_folder = "Argonium_Final_Project"
        for path, directories, files in os.walk('C:\\'):
            if game_folder in directories:
                Images.PATHS.append(os.path.join(path, game_folder) + "\\Pictures\\")

        Images.FIGHTER_PATHS.append(path + "fighter\\" for path in Images.PATHS)
        Images.MAPS_PATHS.append(path + "maps\\" for path in Images.PATHS)

        for i in range(4):
            Images.FIGHTER_MOVE_UP_IMAGES.append(path + "move_U\\U_" + str(i) + ".png" for path in Images.FIGHTER_PATHS)
            Images.FIGHTER_MOVE_RIGHT_IMAGES.append(path + "move_R\\R_" + str(i) + ".png" for path in Images.FIGHTER_PATHS)
            Images.FIGHTER_MOVE_DOWN_IMAGES.append(path + "move_D\\D_" + str(i) + ".png" for path in Images.FIGHTER_PATHS)
            Images.FIGHTER_MOVE_LEFT_IMAGES.append(path + "move_L\\L_" + str(i) + ".png" for path in Images.FIGHTER_PATHS)

        Images.MAP_TOWN_PATHS.append(path + "town.tmx" for path in Images.MAPS_PATHS)



