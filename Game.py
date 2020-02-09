import socket
import pygame
from Commands import Commands
import time
from Connection import Connection
import threading
from Images import Images
from GameActions import GameActions
from queue import Queue
from World import World
from Map import Map


class Game(object):
    def __init__(self):
        Images.load_images()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 1729))
        self.connection = Connection(self.socket)

        self.user_info = None

        self.world = None
        self.current_map_location = [0, 0]
        self.current_map = None

        self.display = None

        self.movement_state = {
            "UP": False,
            "DOWN": False,
            "RIGHT": False,
            "LEFT": False
        }

    def play_game(self):
        self.login()
        self.choose_game()
        self.run_game()

    def login(self):
        logged_in = False
        username = input("Username: ")
        password = input("Password: ")
        msg = [Commands.ATTEMPT_LOGIN, username, password]
        self.connection.send_packed(msg)
        logged_in = self.connection.receive_byte()
        while logged_in == Commands.LOGIN_FAILED:
            msg = self.connection.receive_packed()
            username = input("Username: ")
            password = input("Password: ")
            msg = [Commands.ATTEMPT_LOGIN, username, password]
            self.connection.send_packed(msg)
            logged_in = self.connection.receive_byte()
        self.user_info = self.connection.receive_object()

    def choose_game(self):
        chosen_game = input("Game: ")
        msg = [Commands.ENTER_SESSION, chosen_game]
        self.connection.send_packed(msg)
        self.world = self.connection.receive_object()

    def set_up_game(self):
        print(len(self.world.maps))
        for single_map in self.world.maps:
            single_map.initiate_map()
        # TODO: Load all images as pygame images
        self.current_map = self.world.maps[0]

    def run_game(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Argonium')

        self.set_up_game()

        t2 = threading.Thread(target=self.receive_updates)
        t2.start()
        clock = pygame.time.Clock()

        while True:
            clock.tick(40)
            for event in pygame.event.get():
                # TODO: Change if statements to dictionary
                if event.type == pygame.QUIT:
                    self.connection.send_byte(Commands.QUIT)
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement_state["UP"] = True
                        self.movement_state["DOWN"] = False
                    elif event.key == pygame.K_DOWN:
                        self.movement_state["DOWN"] = True
                        self.movement_state["UP"] = False
                    elif event.key == pygame.K_LEFT:
                        self.movement_state["LEFT"] = True
                        self.movement_state["RIGHT"] = False
                    elif event.key == pygame.K_RIGHT:
                        self.movement_state["RIGHT"] = True
                        self.movement_state["LEFT"] = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement_state["UP"] = False
                    elif event.key == pygame.K_DOWN:
                        self.movement_state["DOWN"] = False
                    elif event.key == pygame.K_LEFT:
                        self.movement_state["LEFT"] = False
                    elif event.key == pygame.K_RIGHT:
                        self.movement_state["RIGHT"] = False

            if self.movement_state["UP"]:
                self.connection.send_byte(GameActions.MOVE_UP)
            elif self.movement_state["DOWN"]:
                self.connection.send_byte(GameActions.MOVE_DOWN)
            if self.movement_state["RIGHT"]:
                self.connection.send_byte(GameActions.MOVE_RIGHT)
            elif self.movement_state["LEFT"]:
                self.connection.send_byte(GameActions.MOVE_LEFT)

            self.display.blit(self.current_map.tiled_map.make_map(), (0, 0))
            for game_object in self.current_map.game_objects:
                self.display.blit(pygame.image.load(game_object.image), [game_object.x, game_object.y]) # TODO: have the image loaded already
            pygame.display.flip()

    def receive_updates(self):
        print("start receive")
        while True:
            update_info_list = self.connection.receive_packed()
            game_action = update_info_list[0]
            object_id = update_info_list[1]
            for single_map in self.world.maps:
                for game_object in single_map.game_objects:
                    if object_id == game_object.id:
                        game_object.update(game_action)


def main():
    game = Game()
    game.play_game()


if __name__ == '__main__':
    main()
