import pygame
from Images import Images
from GameActions import GameActions


class PlayerCharacter(pygame.sprite.Sprite):
    ID = 0

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.pc_id = PlayerCharacter.ID
        PlayerCharacter.ID += 1

        self.world_id = 0
        self.current_map = 0

        self.move_up_images = None  # 4 images
        self.move_down_images = None  # 4 images
        self.move_right_images = None  # 4 images
        self.move_left_images = None  # 4 images

        self.image_index = 0

        self.level = 1
        self.hp = None
        self.mp = None
        self.melee_damage = None
        self.magic_power = None
        self.movement_speed = 20
        self.alive = True

        self.width = None
        self.height = None

        self.x = 50
        self.y = 250

        self.is_moving = False
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self, game_action):
        if game_action == GameActions.MOVE_UP:
            self.y -= self.movement_speed
            self.image = self.move_up_images[self.image_index]
            if self.image_index == 3:
                self.image_index = 0
            else:
                self.image_index += 1
        elif game_action == GameActions.MOVE_DOWN:
            self.y += self.movement_speed
            self.image = self.move_down_images[self.image_index]
            if self.image_index == 3:
                self.image_index = 0
            else:
                self.image_index += 1
        elif game_action == GameActions.MOVE_RIGHT:
            self.x += self.movement_speed
            self.image = self.move_right_images[self.image_index]
            if self.image_index == 3:
                self.image_index = 0
            else:
                self.image_index += 1
        elif game_action == GameActions.MOVE_LEFT:
            self.x -= self.movement_speed
            self.image = self.move_left_images[self.image_index]
            if self.image_index == 3:
                self.image_index = 0
            else:
                self.image_index += 1

        elif game_action == GameActions.STOP_MOVE_UP:
            self.moving_up = False
        elif game_action == GameActions.STOP_MOVE_DOWN:
            self.moving_down = False
        elif game_action == GameActions.STOP_MOVE_RIGHT:
            self.moving_right = False
        elif game_action == GameActions.STOP_MOVE_LEFT:
            self.moving_left = False


class FighterClass(PlayerCharacter):
    CLASS_NAME = "Fighter"

    def __init__(self, user_id):
        super().__init__(user_id)
        self.move_up_images = Images.FIGHTER_MOVE_UP_IMAGES  # 4 images
        self.move_down_images = Images.FIGHTER_MOVE_DOWN_IMAGES  # 4 images
        self.move_right_images = Images.FIGHTER_MOVE_RIGHT_IMAGES  # 4 images
        self.move_left_images = Images.FIGHTER_MOVE_LEFT_IMAGES  # 4 images
        self.image = self.move_up_images[self.image_index]

