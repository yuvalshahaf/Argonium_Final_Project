import os


class Images:
    PATH = ""

    FIGHTER_PATH = ""
    FIGHTER_MOVE_UP_IMAGES = []
    FIGHTER_MOVE_DOWN_IMAGES = []
    FIGHTER_MOVE_RIGHT_IMAGES = []
    FIGHTER_MOVE_LEFT_IMAGES = []

    MAPS_PATH = ""
    MAP_TOWN = ""

    @staticmethod
    def load_images():
        game_folder = "Argonuim_Final_Project"
        for path, directories, files in os.walk('C:\\'):
            if game_folder in directories:
                Images.PATH = os.path.join(path, game_folder) + "\\Pictures\\"

        Images.FIGHTER_PATH = Images.PATH + "fighter\\"
        Images.MAPS_PATH = Images.PATH + "maps\\"

        for i in range(4):
            Images.FIGHTER_MOVE_UP_IMAGES.append(Images.FIGHTER_PATH + "move_U\\U_" + str(i) + ".png")
            Images.FIGHTER_MOVE_RIGHT_IMAGES.append(Images.FIGHTER_PATH + "move_R\\R_" + str(i) + ".png")
            Images.FIGHTER_MOVE_DOWN_IMAGES.append(Images.FIGHTER_PATH + "move_D\\D_" + str(i) + ".png")
            Images.FIGHTER_MOVE_LEFT_IMAGES.append(Images.FIGHTER_PATH + "move_L\\L_" + str(i) + ".png")

        Images.MAP_TOWN = Images.MAPS_PATH + "town.tmx"



