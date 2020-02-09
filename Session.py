import pygame
from GameActions import GameActions
import queue
from functools import partial
import threading
from Client import Client


class Session(object):
    def __init__(self, world):
        self.clients = []
        self.received_actions_queue = queue.Queue()
        self.world = world
        self.players_characters = [self.world.maps[0].game_objects[0]]
        t1 = threading.Thread(target=self.calculate_actions)
        t1.start()

    def connect_client(self, client):
        client.connection.send_object(self.world)
        self.clients.append(client)
        receive_from_client_thread = threading.Thread(target=self.receive_action_from_client, args=(client,))
        receive_from_client_thread.start()

    def receive_action_from_client(self, client):
        while True:
            action = client.connection.receive_byte()
            for pc in self.players_characters:
                if pc.pc_id == client.current_character_id:
                    self.received_actions_queue.put((action, pc))

    def calculate_actions(self):
        while True:
            update = None
            action_info_list = self.received_actions_queue.get()
            current_action = action_info_list[0]
            player_character = action_info_list[1]
            if current_action == GameActions.MOVE_UP:
                player_character.y -= player_character.movement_speed
                player_character.moving_up = True
                player_character.moving_down = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.MOVE_DOWN:
                player_character.y += player_character.movement_speed
                player_character.moving_down = True
                player_character.moving_up = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.MOVE_LEFT:
                player_character.x -= player_character.movement_speed
                player_character.moving_left = True
                player_character.moving_right = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.MOVE_RIGHT:
                player_character.x += player_character.movement_speed
                player_character.moving_right = True
                player_character.moving_left = False
                update = [current_action, player_character.id]

            elif current_action == GameActions.STOP_MOVE_UP:
                player_character.moving_up = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.STOP_MOVE_DOWN:
                player_character.moving_down = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.STOP_MOVE_LEFT:
                player_character.moving_left = False
                update = [current_action, player_character.id]
            elif current_action == GameActions.STOP_MOVE_RIGHT:
                player_character.moving_right = False
                update = [current_action, player_character.id]
            if update is not None:
                for client in self.clients:
                    client.connection.send_packed(update)

    def calculate_collisions(self, game_object, source):
        for person in source.current_map.all:
            if person != game_object:
                if self.is_collision(game_object, person):
                    person.hp = person.hp - game_object.damage

    def is_collision(self, game_object, person):
        if (abs(game_object.x - person.x) < game_object.width) and (abs(game_object.y - person.y) < game_object.height):
            return True
        return False
