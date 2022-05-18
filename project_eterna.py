import random
import time
import pygame
import pickle
from pygame.locals import *

import click_handlers
import gameplay_functions
import resource_urls
import drawing_functions

# global variables -----------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
velocity = 2


# class objects --------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, name, race, role, items, p_equipment, current_quests, quest_progress, quest_status,
                 quest_complete, knowledge, skills_mage, skills_fighter, skills_scout, level, experience, health,
                 energy, alive_status, rupees, reputation, current_zone, defense, offense):
        super(Player, self).__init__()
        self.x_coordinate = 760
        self.y_coordinate = 510
        self.surf = player_no_role_amuna_down_1
        self.rect = self.surf.get_rect(center=(self.x_coordinate, self.y_coordinate))
        self.name = name
        self.race = race
        self.role = role
        self.items = items
        self.equipment = p_equipment
        self.current_quests = current_quests
        self.quest_progress = quest_progress
        self.quest_status = quest_status
        self.quest_complete = quest_complete
        self.knowledge = knowledge
        self.skills_mage = skills_mage
        self.skills_fighter = skills_fighter
        self.skills_scout = skills_scout
        self.level = level
        self.experience = experience
        self.health = health
        self.energy = energy
        self.alive_status = alive_status
        self.rupees = rupees
        self.reputation = reputation
        self.current_zone = current_zone
        self.defence = defense
        self.offense = offense

    # move the player sprite based on input keys
    def update(self, pressed_key, current_zone, walk_timed):
        # w key is pressed to move player up. set surface based on race, role and current animation. set y value -
        if pressed_key == "up":
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "amuna":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_amuna_up_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_amuna_up_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_amuna_up_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_amuna_up_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_amuna_up_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_amuna_up_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_amuna_up_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_amuna_up_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_amuna_up_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_amuna_up_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_amuna_up_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_amuna_up_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_amuna_up_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_amuna_up_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_amuna_up_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_amuna_up_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "sorae":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_sorae_up_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_sorae_up_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_sorae_up_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_sorae_up_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_sorae_up_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_sorae_up_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_sorae_up_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_sorae_up_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_sorae_up_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_sorae_up_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_sorae_up_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_sorae_up_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_sorae_up_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_sorae_up_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_sorae_up_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_sorae_up_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "nuldar":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_nuldar_up_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_nuldar_up_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_nuldar_up_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_nuldar_up_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_nuldar_up_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_nuldar_up_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_nuldar_up_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_nuldar_up_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_nuldar_up_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_nuldar_up_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_nuldar_up_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_nuldar_up_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_nuldar_up_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_nuldar_up_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_nuldar_up_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_nuldar_up_4
            self.y_coordinate -= velocity

        # s key is pressed to move player down. set surface based on race, role and current animation. set y value +
        if pressed_key == "down":
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "amuna":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_amuna_down_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_amuna_down_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_amuna_down_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_amuna_down_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_amuna_down_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_amuna_down_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_amuna_down_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_amuna_down_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_amuna_down_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_amuna_down_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_amuna_down_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_amuna_down_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_amuna_down_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_amuna_down_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_amuna_down_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_amuna_down_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "sorae":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_sorae_down_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_sorae_down_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_sorae_down_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_sorae_down_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_sorae_down_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_sorae_down_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_sorae_down_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_sorae_down_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_sorae_down_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_sorae_down_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_sorae_down_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_sorae_down_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_sorae_down_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_sorae_down_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_sorae_down_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_sorae_down_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "nuldar":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_nuldar_down_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_nuldar_down_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_nuldar_down_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_nuldar_down_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_nuldar_down_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_nuldar_down_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_nuldar_down_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_nuldar_down_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_nuldar_down_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_nuldar_down_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_nuldar_down_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_nuldar_down_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_nuldar_down_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_nuldar_down_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_nuldar_down_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_nuldar_down_4
            self.y_coordinate += velocity

        # a key is pressed to move player left. set surface based on race, role and current animation. set x value -
        if pressed_key == "left":
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "amuna":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_amuna_left_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_amuna_left_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_amuna_left_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_amuna_left_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_amuna_left_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_amuna_left_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_amuna_left_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_amuna_left_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_amuna_left_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_amuna_left_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_amuna_left_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_amuna_left_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_amuna_left_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_amuna_left_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_amuna_left_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_amuna_left_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "sorae":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_sorae_left_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_sorae_left_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_sorae_left_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_sorae_left_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_sorae_left_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_sorae_left_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_sorae_left_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_sorae_left_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_sorae_left_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_sorae_left_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_sorae_left_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_sorae_left_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_sorae_left_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_sorae_left_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_sorae_left_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_sorae_left_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "nuldar":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_nuldar_left_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_nuldar_left_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_nuldar_left_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_nuldar_left_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_nuldar_left_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_nuldar_left_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_nuldar_left_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_nuldar_left_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_nuldar_left_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_nuldar_left_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_nuldar_left_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_nuldar_left_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_nuldar_left_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_nuldar_left_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_nuldar_left_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_nuldar_left_4
            self.x_coordinate -= velocity

        # d key is pressed to move player right. set surface based on race, role and current animation. set x value +
        if pressed_key == "right":
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "amuna":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_amuna_right_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_amuna_right_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_amuna_right_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_amuna_right_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_amuna_right_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_amuna_right_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_amuna_right_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_amuna_right_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_amuna_right_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_amuna_right_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_amuna_right_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_amuna_right_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_amuna_right_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_amuna_right_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_amuna_right_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_amuna_right_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "sorae":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_sorae_right_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_sorae_right_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_sorae_right_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_sorae_right_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_sorae_right_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_sorae_right_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_sorae_right_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_sorae_right_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_sorae_right_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_sorae_right_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_sorae_right_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_sorae_right_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_sorae_right_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_sorae_right_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_sorae_right_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_sorae_right_4
            # ----------------------------------------------------------------------------------------------------------
            if player.race == "nuldar":
                if player.role == "mage":
                    if walk_timed < 0.2:
                        self.surf = player_mage_nuldar_right_1
                    if walk_timed > 0.2:
                        self.surf = player_mage_nuldar_right_2
                    if walk_timed > 0.4:
                        self.surf = player_mage_nuldar_right_3
                    if walk_timed > 0.6:
                        self.surf = player_mage_nuldar_right_4
                if player.role == "fighter":
                    if walk_timed < 0.2:
                        self.surf = player_fighter_nuldar_right_1
                    if walk_timed > 0.2:
                        self.surf = player_fighter_nuldar_right_2
                    if walk_timed > 0.4:
                        self.surf = player_fighter_nuldar_right_3
                    if walk_timed > 0.6:
                        self.surf = player_fighter_nuldar_right_4
                if player.role == "scout":
                    if walk_timed < 0.2:
                        self.surf = player_scout_nuldar_right_1
                    if walk_timed > 0.2:
                        self.surf = player_scout_nuldar_right_2
                    if walk_timed > 0.4:
                        self.surf = player_scout_nuldar_right_3
                    if walk_timed > 0.6:
                        self.surf = player_scout_nuldar_right_4
                if player.role == "":
                    if walk_timed < 0.2:
                        self.surf = player_no_role_nuldar_right_1
                    if walk_timed > 0.2:
                        self.surf = player_no_role_nuldar_right_2
                    if walk_timed > 0.4:
                        self.surf = player_no_role_nuldar_right_3
                    if walk_timed > 0.6:
                        self.surf = player_no_role_nuldar_right_4
            self.x_coordinate += velocity

        # keep player on the screen, boundaries vary depending on current zone
        if current_zone == "nascent":
            if self.x_coordinate < 340:
                self.x_coordinate = 340
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 60:
                self.y_coordinate = 60
            elif self.y_coordinate >= SCREEN_HEIGHT - 50:
                self.y_coordinate = SCREEN_HEIGHT - 50
            # for wall/gate collision in nascent grove/starting area
            elif 315 >= self.y_coordinate >= 300:
                self.y_coordinate = 315
            elif 300 >= self.y_coordinate >= 230:
                self.y_coordinate = 230
        if current_zone == "seldon":
            if self.x_coordinate < 15:
                self.x_coordinate = 15
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5
        if current_zone == "stardust":
            if self.x_coordinate < 225:
                self.x_coordinate = 225
            elif self.x_coordinate > SCREEN_WIDTH - 325:
                self.x_coordinate = SCREEN_WIDTH - 325
            if self.y_coordinate <= 80:
                self.y_coordinate = 80
            elif self.y_coordinate >= SCREEN_HEIGHT - 80:
                self.y_coordinate = SCREEN_HEIGHT - 80
            # for stardust outpost collision, bigger building
            elif 360 >= self.y_coordinate >= 300 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 360
            elif 300 >= self.y_coordinate >= 230 and 641 >= self.x_coordinate >= 409:
                self.y_coordinate = 230
            elif 645 >= self.x_coordinate >= 500 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 645
            elif 500 >= self.x_coordinate >= 395 and 358 >= self.y_coordinate >= 232:
                self.x_coordinate = 395
        if current_zone == "korlok":
            if self.x_coordinate < 25:
                self.x_coordinate = 25
            elif self.x_coordinate > SCREEN_WIDTH - 355:
                self.x_coordinate = SCREEN_WIDTH - 355
            if self.y_coordinate <= 115:
                self.y_coordinate = 115
            elif self.y_coordinate >= SCREEN_HEIGHT - 5:
                self.y_coordinate = SCREEN_HEIGHT - 5

        if current_zone == "seldon":
            collided = pygame.sprite.spritecollideany(player, environments, pygame.sprite.collide_rect_ratio(0.50))
            if collided:
                if player.x_coordinate < collided.x_coordinate:
                    self.x_coordinate -= velocity
                if player.x_coordinate > collided.x_coordinate:
                    self.x_coordinate += velocity
                if player.y_coordinate < collided.y_coordinate:
                    self.y_coordinate -= velocity
                if player.y_coordinate > collided.y_coordinate:
                    self.y_coordinate += velocity


# any in game npc. can have quests and also gifts to player upon initial interaction
class NPC(pygame.sprite.Sprite):
    def __init__(self, name, gender, race, role, dialog, quest_to_give, quest_description, x_coordinate, y_coordinate,
                 alive_status, quest_complete, items, gift, image):
        super(NPC, self).__init__()
        self.name = name
        self.gender = gender
        self.race = race
        self.role = role
        self.dialog = dialog
        self.quest_to_give = quest_to_give
        self.quest_description = quest_description
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.alive_status = alive_status
        self.quest_complete = quest_complete
        self.items = items
        self.gift = gift
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, image):
        self.surf = image


# shopkeeper class for assigning attributed items in shop
class Shopkeeper(pygame.sprite.Sprite):
    def __init__(self, name, race, items):
        super(Shopkeeper, self).__init__()
        self.name = name
        self.race = race
        self.items = items


# enemy class used for any enemy like snakes, ghouls etc
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image,
                 health_bar):
        super(Enemy, self).__init__()
        self.name = name
        self.kind = kind
        self.health = health
        self.energy = energy
        self.level = level
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.alive_status = alive_status
        self.items = items
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))
        self.speed = 1
        self.health_bar = health_bar

    # updates enemy image
    def update_image(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))

    # updates enemy map position
    def update_position(self, ranges_x, ranges_y, direction_x, direction_y):
        if ranges_x[0] < self.rect.x < ranges_x[1]:
            if direction_x == "left":
                self.rect.move_ip(-1, 0)
            if direction_x == "right":
                self.rect.move_ip(1, 0)
        else:
            if direction_x == "left":
                self.rect.move_ip(1, 0)
            if direction_x == "right":
                self.rect.move_ip(-1, 0)
        if ranges_y[0] < self.rect.x < ranges_y[1]:
            if direction_y == "down":
                self.rect.move_ip(0, -1)
            if direction_y == "up":
                self.rect.move_ip(0, 1)
        else:
            if direction_y == "down":
                self.rect.move_ip(0, 1)
            if direction_y == "up":
                self.rect.move_ip(0, -1)


# tree or tree-like sprites. collision checks
class Tree(pygame.sprite.Sprite):
    def __init__(self, name, model, x_coordinate, y_coordinate, gathered, image):
        super(Tree, self).__init__()
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.gathered = gathered
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# building sprite. collision checks
class Building(pygame.sprite.Sprite):
    def __init__(self, name, model, x_coordinate, y_coordinate, image):
        super(Building, self).__init__()
        self.name = name
        self.model = model
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# any UI element like buttons, bars, player status etc
class UiElement(pygame.sprite.Sprite):
    def __init__(self, name, x_coordinate, y_coordinate, image):
        super(UiElement, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# inventory class used for shop
class Inventory(pygame.sprite.Sprite):
    def __init__(self, name, contains, x_coordinate, y_coordinate, image):
        super(Inventory, self).__init__()
        self.name = name
        self.contains = contains
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# pop up notifications
class Notification(pygame.sprite.Sprite):
    def __init__(self, name, shown, x_coordinate, y_coordinate, image):
        super(Notification, self).__init__()
        self.name = name
        self.shown = shown
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# representation of character for battle screen or npc interaction
class BattleCharacter(pygame.sprite.Sprite):
    def __init__(self, name, x_coordinate, y_coordinate, image):
        super(BattleCharacter, self).__init__()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# any item or equipment
class Item(pygame.sprite.Sprite):
    def __init__(self, name, type, x_coordinate, y_coordinate, image):
        super(Item, self).__init__()
        self.name = name
        self.type = type
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coordinate, y_coordinate))

    def update(self, x_coord, y_coord, image):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.surf = image
        self.rect = self.surf.get_rect(center=(x_coord, y_coord))


# sprite sheet class. load the sheet, set color key. create a transparent surface for new image with get_image
class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite_sheet.set_colorkey((255, 255, 255), RLEACCEL)

    def get_image(self, x, y, width, height):
        sprite_image = pygame.Surface([width, height], pygame.SRCALPHA)
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite_image


# gameplay functions ---------------------------------------------------------------------------------------------------
def attack_scenario(enemy_combating, combat_event):
    # get the all the stuff that happened in this scenario and return it to main loop via dictionary keys and values
    combat_event_dictionary = {
        "damage done": 0, "damage taken": 0,
        "item dropped": "", "experience gained": 0,
        "quest update": "", "enemy defeated": False, "escaped": False,
        "level up status": "", "level up attributes": ""
    }
    if combat_event == "attack":
        if enemy_combating.alive_status:
            # returns players damage to the enemy based on level and equipment
            attacked_enemy_health = attack_enemy(enemy_combating)
            enemy_combating.health = enemy_combating.health - attacked_enemy_health
            try:
                enemy_combating.health_bar.update(enemy_combating.health_bar.x_coordinate,
                                                  enemy_combating.health_bar.y_coordinate,
                                                  health_bar_update(enemy_combating))
            except AttributeError:
                pass

            # if enemy is not dead yet
            if enemy_combating.health > 0:
                attacked_enemy_string = f" You did {attacked_enemy_health} damage to {enemy_combating.name}."
                # add damage to enemy to event dictionary to be returned to main loop
                combat_event_dictionary["damage done"] = attacked_enemy_string
                # returns total damage output from enemy as attacked_player_health value
                attacked_player_health = attack_player(enemy_combating)
                if attacked_player_health > 0:
                    attacked_player_string = f"You take {attacked_player_health} damage from {enemy_combating.name}."
                    player.health = player.health - attacked_player_health
                    # add damage done to player from enemy to dictionary
                    combat_event_dictionary["damage taken"] = attacked_player_string

                    # player health is less than or equal to 0, player is dead
                    if player.health <= 0:
                        player.alive_status = False
                    return combat_event_dictionary
                else:
                    enemy_miss_string = f'{enemy_combating.name} missed.'
                    # add to dictionary that enemy did no damage to player
                    combat_event_dictionary["damage taken"] = enemy_miss_string
                    return combat_event_dictionary

            # enemy has been defeated, will return an amount of xp based on current levels
            else:
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.quest_status["sneaky snakes"]:
                        if player.quest_progress["sneaky snakes"] < 4:
                            player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                            quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.quest_status["ghouled again"]:
                        if player.quest_progress["ghouled again"] < 4:
                            player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                            quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # experienced gained by player from defeating enemy
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 25)
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience} xp "
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience

                drop_chance = random.randrange(1, 10)
                # 80% chance (roughly?) to drop merchant item sellable by player for rupees at shops
                if drop_chance > 2:

                    # doesn't give item to player if their inventory is full
                    if len(player.items) < 16:
                        player.items.append(enemy_combating.items)
                        enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                        # add to dictionary anything dropped from enemy upon their defeat
                        combat_event_dictionary["item dropped"] = enemy_dropped_this
                    else:
                        combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                else:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up if experience greater than or equal to 100
                if player.experience >= 100:
                    gameplay_functions.level_up(player)

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated
                combat_event_dictionary["enemy defeated"] = True
                return combat_event_dictionary
        else:
            print("\nThis enemy appears to be dead already!")

    # active combat skill, if player is fighter and has learned hard strike from the academia
    # same as default attack from above, but attack replaced by hard strike skill
    if combat_event == "skill 1":
        if player.role == "fighter":
            if hard_strike_learned:
                if enemy_combating.alive_status:
                    striked = random.randrange(20, 40)  # hard strike damage
                    enemy_combating.health = enemy_combating.health - striked
                    try:
                        enemy_combating.health_bar.update(enemy_combating.health_bar.x_coordinate,
                                                          enemy_combating.health_bar.y_coordinate,
                                                          health_bar_update(enemy_combating))
                    except AttributeError:
                        pass
                    if enemy_combating.health > 0:
                        attacked_enemy_string = f"Hard strike did {striked} damage!"
                        combat_event_dictionary["damage done"] = attacked_enemy_string
                        attacked_player_health = attack_player(enemy_combating)
                        if attacked_player_health > 0:
                            attacked_player_string = f"You take {attacked_player_health} damage from " \
                                                     f"{enemy_combating.name}."
                            player.health = player.health - attacked_player_health
                            combat_event_dictionary["damage taken"] = attacked_player_string
                            if player.health <= 0:
                                player.alive_status = False
                            return combat_event_dictionary
                        else:
                            enemy_miss_string = f'{enemy_combating.name} missed.'
                            combat_event_dictionary["damage taken"] = enemy_miss_string
                            return combat_event_dictionary
                    else:
                        if enemy_combating.kind == "snake":
                            if player.quest_status["sneaky snakes"]:
                                if player.quest_progress["sneaky snakes"] < 4:
                                    player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                                    quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        if enemy_combating.kind == "ghoul":
                            if player.quest_status["ghouled again"]:
                                if player.quest_progress["ghouled again"] < 4:
                                    player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                                    quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        if player.level <= enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level) * 35)
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience} xp "
                            combat_event_dictionary["experience gained"] = enemy_experience
                        drop_chance = random.randrange(1, 10)
                        if drop_chance > 2:
                            if len(player.items) < 16:
                                player.items.append(enemy_combating.items)
                                enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                                combat_event_dictionary["item dropped"] = enemy_dropped_this
                            else:
                                combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                        else:
                            combat_event_dictionary["item dropped"] = "No"
                        if player.experience >= 100:
                            gameplay_functions.level_up(player)
                        enemy_combating.alive_status = False
                        enemy_combating.kill()
                        combat_event_dictionary["enemy defeated"] = True
                        return combat_event_dictionary
                else:
                    print("\nThis enemy appears to be dead already!")


# player attacks enemy, gets damage to enemy done based on player's role and offense
def attack_enemy(mob):
    # if player is lower level than mob, scale their damage based on the difference of their levels
    if player.level < mob.level:
        difference = mob.level - player.level
    # if player is equal level or higher level than mob, just return full damage value
    else:
        difference = 1
    # scale damage based on player's offense stat and level difference
    if player.role == "mage":
        damage = (random.randrange(17, player.offense) // difference)
    if player.role == "scout":
        damage = (random.randrange(12, player.offense) // difference)
    if player.role == "fighter":
        damage = (random.randrange(7, player.offense) // difference)
    if player.role == "":
        damage = (random.randrange(1, 7) // difference)

    return damage


# enemy attacks player, gets damage to player done, subtract players defense level
def attack_player(mob):
    base_damage = (random.randrange(10, 18))
    difference = mob.level - player.level
    # add additional damage if enemy is a higher level than player
    if difference >= 1:
        base_damage = base_damage + 3
    if difference >= 2:
        base_damage = base_damage + 5
    if difference >= 3:
        base_damage = base_damage + 8
    final_damage = base_damage - player.defence

    return final_damage


# player health bar update function. return image representing amount
def health_bar_update(character):
    return gameplay_functions.health_bar_update(character,
                                                hp_100, hp_99, hp_98, hp_97, hp_96, hp_95, hp_94, hp_93, hp_92, hp_91,
                                                hp_90, hp_89, hp_88, hp_87, hp_86, hp_85, hp_84, hp_83, hp_82, hp_81,
                                                hp_80, hp_79, hp_78, hp_77, hp_76, hp_75, hp_74, hp_73, hp_72, hp_71,
                                                hp_70, hp_69, hp_68, hp_67, hp_66, hp_65, hp_64, hp_63, hp_62, hp_61,
                                                hp_60, hp_59, hp_58, hp_57, hp_56, hp_55, hp_54, hp_53, hp_52, hp_51,
                                                hp_50, hp_49, hp_48, hp_47, hp_46, hp_45, hp_44, hp_43, hp_42, hp_41,
                                                hp_40, hp_39, hp_38, hp_37, hp_36, hp_35, hp_34, hp_33, hp_32, hp_31,
                                                hp_30, hp_29, hp_28, hp_27, hp_26, hp_25, hp_24, hp_23, hp_22, hp_21,
                                                hp_20, hp_19, hp_18, hp_17, hp_16, hp_15, hp_14, hp_13, hp_12, hp_11,
                                                hp_10, hp_9, hp_8, hp_7, hp_6, hp_5, hp_4, hp_3, hp_2, hp_1, hp_0)


# player energy bar update function. return image representing amount
def energy_bar_update(character):
    return gameplay_functions.energy_bar_update(character,
                                                en_100, en_99, en_98, en_97, en_96, en_95, en_94, en_93, en_92, en_91,
                                                en_90, en_89, en_88, en_87, en_86, en_85, en_84, en_83, en_82, en_81,
                                                en_80, en_79, en_78, en_77, en_76, en_75, en_74, en_73, en_72, en_71,
                                                en_70, en_69, en_68, en_67, en_66, en_65, en_64, en_63, en_62, en_61,
                                                en_60, en_59, en_58, en_57, en_56, en_55, en_54, en_53, en_52, en_51,
                                                en_50, en_49, en_48, en_47, en_46, en_45, en_44, en_43, en_42, en_41,
                                                en_40, en_39, en_38, en_37, en_36, en_35, en_34, en_33, en_32, en_31,
                                                en_30, en_29, en_28, en_27, en_26, en_25, en_24, en_23, en_22, en_21,
                                                en_20, en_19, en_18, en_17, en_16, en_15, en_14, en_13, en_12, en_11,
                                                en_10, en_9, en_8, en_7, en_6, en_5, en_4, en_3, en_2, en_1, en_0)


# player xp bar update function. return image representing amount
def xp_bar_update(character):
    return gameplay_functions.xp_bar_update(character,
                                            xp_100, xp_99, xp_98, xp_97, xp_96, xp_95, xp_94, xp_93, xp_92, xp_91,
                                            xp_90, xp_89, xp_88, xp_87, xp_86, xp_85, xp_84, xp_83, xp_82, xp_81,
                                            xp_80, xp_79, xp_78, xp_77, xp_76, xp_75, xp_74, xp_73, xp_72, xp_71,
                                            xp_70, xp_69, xp_68, xp_67, xp_66, xp_65, xp_64, xp_63, xp_62, xp_61,
                                            xp_60, xp_59, xp_58, xp_57, xp_56, xp_55, xp_54, xp_53, xp_52, xp_51,
                                            xp_50, xp_49, xp_48, xp_47, xp_46, xp_45, xp_44, xp_43, xp_42, xp_41,
                                            xp_40, xp_39, xp_38, xp_37, xp_36, xp_35, xp_34, xp_33, xp_32, xp_31,
                                            xp_30, xp_29, xp_28, xp_27, xp_26, xp_25, xp_24, xp_23, xp_22, xp_21,
                                            xp_20, xp_19, xp_18, xp_17, xp_16, xp_15, xp_14, xp_13, xp_12, xp_11,
                                            xp_10, xp_9, xp_8, xp_7, xp_6, xp_5, xp_4, xp_3, xp_2, xp_1, xp_0)


# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn():
    snake_counter = 0
    ghoul_counter = 0
    # generate random coordinates and level for new enemy to spawn within boundaries and level range
    # if not scaled, coordinates set to default boundaries
    random_snake_x = random.randrange(150, 300)
    random_snake_y = random.randrange(150, 300)
    random_snake_level = random.randrange(1, 3)
    random_ghoul_x = random.randrange(650, 900)
    random_ghoul_y = random.randrange(150, 300)
    random_ghoul_level = random.randrange(3, 6)

    # count current enemies active in game
    for mob in enemies:
        if mob.name == "snake":
            snake_counter += 1
        if mob.name == "ghoul":
            ghoul_counter += 1

    # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
    if snake_counter < 3:
        new_snake = Enemy("snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y, True,
                          Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                          UiElement("snake hp bar", 700, 90, hp_100))
        snakes.add(new_snake)
        enemies.add(new_snake)
        most_sprites.add(new_snake)

    # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
    if ghoul_counter < 3:
        new_ghoul = Enemy("ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                          Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                          UiElement("ghoul hp bar", 700, 90, hp_100))
        ghouls.add(new_ghoul)
        enemies.add(new_ghoul)
        most_sprites.add(new_ghoul)


# save game function. stores player info in a dictionary that's serialized and saved to save_game file
def save_game():
    inventory_save = []
    equipment_save = []
    # a sprite surface object cannot be serialized, so save the string item name instead
    try:
        for item_x in player.items:
            inventory_save.append(item_x.name)
        equipment_save.append(player.equipment["weapon"].name)
        equipment_save.append(player.equipment["chest"].name)
    except AttributeError:
        pass
    player_save_info = {"name": str(player.name), "race": str(player.race),
                        "level": int(player.level), "role": str(player.role),
                        "inventory": inventory_save, "equipment": equipment_save,
                        "hp": int(player.health), "en": int(player.energy), "xp": int(player.experience),
                        "offense": int(player.offense), "defense": int(player.defence),
                        "quests": dict(player.current_quests),
                        "quest progress": dict(player.quest_progress),
                        "quest status": dict(player.quest_status),
                        "quest complete": dict(player.quest_complete),
                        "knowledge": dict(player.knowledge),
                        "mage skills": dict(player.skills_mage),
                        "fighter skills": dict(player.skills_fighter),
                        "scout skills": dict(player.skills_scout),
                        "learned": {"barrier": barrier_learned,
                                    "strike": hard_strike_learned,
                                    "sense": sharp_sense_learned},
                        "rupees": int(player.rupees), "reputation": dict(player.reputation),
                        "zone": str(player.current_zone), "saved": saved}
    # serialize dictionary and save to file ("save game") with python pickle (wb = write binary)
    with open("save_game", "wb") as ff:
        pickle.dump(player_save_info, ff)


# function to handle player walking animation with time values
def walk_time(tic):
    walk_dict = {"total time": 0, "reset": False}
    toc = time.perf_counter()
    walk_dict["total time"] = toc - tic
    if walk_dict["total time"] > 0.8:
        walk_dict["reset"] = True

    return walk_dict


# function that updates players info, status, role, inventory, equipment, etc
def player_info_and_ui_updates():
    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    # update players status bars
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player))
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player))
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player))

    if in_over_world:
        screen.blit(player.surf, player.rect)
        for ui_elements in user_interface:
            screen.blit(ui_elements.surf, ui_elements.rect)
        for save_window in save_check_window:
            screen.blit(save_window.surf, save_window.rect)

    # draw texts to the screen, like message box, player rupees and level
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4)
    # update players current equipment
    drawing_functions.equipment_updates(player, basic_staff_img, basic_sword_img, basic_bow_img,
                                        basic_robes_img, basic_armor_img, basic_tunic_img)
    # update players current inventory
    drawing_functions.item_updates(player, health_pot_img, energy_pot_img, shiny_rock_img, bone_dust_img,
                                   basic_staff_img, basic_sword_img, basic_bow_img,
                                   basic_robes_img, basic_armor_img, basic_tunic_img, temp_img)
    drawing_functions.draw_it(screen)


# pygame.mixer.init()
# initialize game, set clock for framerate, set screen size
pygame.init()
pygame.display.set_caption("Project Eterna")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# background textures --------------------------------------------------------------------------------------------------
nascent_grove_bg = pygame.image.load(resource_urls.nascent_grove_screen)
seldon_district_bg = pygame.image.load(resource_urls.seldon_bg_screen)
seldon_district_battle = pygame.image.load(resource_urls.seldon_battle_screen)
seldon_district_shop = pygame.image.load(resource_urls.seldon_shop_screen)
seldon_district_inn = pygame.image.load(resource_urls.seldon_inn_screen)
seldon_district_academia = pygame.image.load(resource_urls.seldon_academia_screen)
stardust_outpost_bg = pygame.image.load(resource_urls.stardust_outpost_screen)
seldon_hearth_screen = pygame.image.load(resource_urls.seldon_hearth_screen)
game_over_screen = pygame.image.load(resource_urls.game_over_screen)
start_screen = pygame.image.load(resource_urls.start_screen)
nera_sleep_screen = pygame.image.load(resource_urls.nera_sleep_screen)
korlok_district_bg = pygame.image.load(resource_urls.korlok_bg_screen)
amuna_character_screen = pygame.image.load(resource_urls.amuna_character_screen)
nuldar_character_screen = pygame.image.load(resource_urls.nuldar_character_screen)
sorae_character_screen = pygame.image.load(resource_urls.sorae_character_screen)

# sprite sheets --------------------------------------------------------------------------------------------------------
# character lore overlays
race_overlay_sheet = SpriteSheet(resource_urls.race_select_overlays_url)
amuna_overlay_img = race_overlay_sheet.get_image(0, 0, 278, 372)
nuldar_overlay_img = race_overlay_sheet.get_image(278, 0, 278, 372)
sorae_overlay_img = race_overlay_sheet.get_image(556, 0, 278, 372)
# character selections
character_select_sheet = SpriteSheet(resource_urls.character_selections)
amuna_character_img = character_select_sheet.get_image(0, 0, 250, 350)
nuldar_character_img = character_select_sheet.get_image(250, 0, 250, 350)
sorae_character_img = character_select_sheet.get_image(500, 0, 250, 350)
# name text box
name_input_sheet = SpriteSheet(resource_urls.name_input_url)
name_input_img = name_input_sheet.get_image(0, 0, 300, 50)
name_input_empty_img = name_input_sheet.get_image(300, 0, 300, 50)
# player no role amuna race
player_no_role_amuna_sheet_down = SpriteSheet(resource_urls.player_no_role_amuna_down_url)
player_no_role_amuna_down_1 = player_no_role_amuna_sheet_down.get_image(0, 0, 50, 75)
player_no_role_amuna_down_2 = player_no_role_amuna_sheet_down.get_image(50, 0, 50, 75)
player_no_role_amuna_down_3 = player_no_role_amuna_sheet_down.get_image(100, 0, 50, 75)
player_no_role_amuna_down_4 = player_no_role_amuna_sheet_down.get_image(150, 0, 50, 75)
player_no_role_amuna_sheet_up = SpriteSheet(resource_urls.player_no_role_amuna_up_url)
player_no_role_amuna_up_1 = player_no_role_amuna_sheet_up.get_image(0, 0, 50, 75)
player_no_role_amuna_up_2 = player_no_role_amuna_sheet_up.get_image(50, 0, 50, 75)
player_no_role_amuna_up_3 = player_no_role_amuna_sheet_up.get_image(100, 0, 50, 75)
player_no_role_amuna_up_4 = player_no_role_amuna_sheet_up.get_image(150, 0, 50, 75)
player_no_role_amuna_sheet_left = SpriteSheet(resource_urls.player_no_role_amuna_left_url)
player_no_role_amuna_left_1 = player_no_role_amuna_sheet_left.get_image(0, 0, 50, 75)
player_no_role_amuna_left_2 = player_no_role_amuna_sheet_left.get_image(50, 0, 50, 75)
player_no_role_amuna_left_3 = player_no_role_amuna_sheet_left.get_image(100, 0, 50, 75)
player_no_role_amuna_left_4 = player_no_role_amuna_sheet_left.get_image(150, 0, 50, 75)
player_no_role_amuna_sheet_right = SpriteSheet(resource_urls.player_no_role_amuna_right_url)
player_no_role_amuna_right_1 = player_no_role_amuna_sheet_right.get_image(0, 0, 50, 75)
player_no_role_amuna_right_2 = player_no_role_amuna_sheet_right.get_image(50, 0, 50, 75)
player_no_role_amuna_right_3 = player_no_role_amuna_sheet_right.get_image(100, 0, 50, 75)
player_no_role_amuna_right_4 = player_no_role_amuna_sheet_right.get_image(150, 0, 50, 75)
# player no role sorae race
player_no_role_sorae_sheet_down = SpriteSheet(resource_urls.player_no_role_sorae_down_url)
player_no_role_sorae_down_1 = player_no_role_sorae_sheet_down.get_image(0, 0, 50, 75)
player_no_role_sorae_down_2 = player_no_role_sorae_sheet_down.get_image(50, 0, 50, 75)
player_no_role_sorae_down_3 = player_no_role_sorae_sheet_down.get_image(100, 0, 50, 75)
player_no_role_sorae_down_4 = player_no_role_sorae_sheet_down.get_image(150, 0, 50, 75)
player_no_role_sorae_sheet_up = SpriteSheet(resource_urls.player_no_role_sorae_up_url)
player_no_role_sorae_up_1 = player_no_role_sorae_sheet_up.get_image(0, 0, 50, 75)
player_no_role_sorae_up_2 = player_no_role_sorae_sheet_up.get_image(50, 0, 50, 75)
player_no_role_sorae_up_3 = player_no_role_sorae_sheet_up.get_image(100, 0, 50, 75)
player_no_role_sorae_up_4 = player_no_role_sorae_sheet_up.get_image(150, 0, 50, 75)
player_no_role_sorae_sheet_left = SpriteSheet(resource_urls.player_no_role_sorae_left_url)
player_no_role_sorae_left_1 = player_no_role_sorae_sheet_left.get_image(0, 0, 50, 75)
player_no_role_sorae_left_2 = player_no_role_sorae_sheet_left.get_image(50, 0, 50, 75)
player_no_role_sorae_left_3 = player_no_role_sorae_sheet_left.get_image(100, 0, 50, 75)
player_no_role_sorae_left_4 = player_no_role_sorae_sheet_left.get_image(150, 0, 50, 75)
player_no_role_sorae_sheet_right = SpriteSheet(resource_urls.player_no_role_sorae_right_url)
player_no_role_sorae_right_1 = player_no_role_sorae_sheet_right.get_image(0, 0, 50, 75)
player_no_role_sorae_right_2 = player_no_role_sorae_sheet_right.get_image(50, 0, 50, 75)
player_no_role_sorae_right_3 = player_no_role_sorae_sheet_right.get_image(100, 0, 50, 75)
player_no_role_sorae_right_4 = player_no_role_sorae_sheet_right.get_image(150, 0, 50, 75)
# player no role nuldar race
player_no_role_nuldar_sheet_down = SpriteSheet(resource_urls.player_no_role_nuldar_down_url)
player_no_role_nuldar_down_1 = player_no_role_nuldar_sheet_down.get_image(0, 0, 50, 75)
player_no_role_nuldar_down_2 = player_no_role_nuldar_sheet_down.get_image(50, 0, 50, 75)
player_no_role_nuldar_down_3 = player_no_role_nuldar_sheet_down.get_image(100, 0, 50, 75)
player_no_role_nuldar_down_4 = player_no_role_nuldar_sheet_down.get_image(150, 0, 50, 75)
player_no_role_nuldar_sheet_up = SpriteSheet(resource_urls.player_no_role_nuldar_up_url)
player_no_role_nuldar_up_1 = player_no_role_nuldar_sheet_up.get_image(0, 0, 50, 75)
player_no_role_nuldar_up_2 = player_no_role_nuldar_sheet_up.get_image(50, 0, 50, 75)
player_no_role_nuldar_up_3 = player_no_role_nuldar_sheet_up.get_image(100, 0, 50, 75)
player_no_role_nuldar_up_4 = player_no_role_nuldar_sheet_up.get_image(150, 0, 50, 75)
player_no_role_nuldar_sheet_left = SpriteSheet(resource_urls.player_no_role_nuldar_left_url)
player_no_role_nuldar_left_1 = player_no_role_nuldar_sheet_left.get_image(0, 0, 50, 75)
player_no_role_nuldar_left_2 = player_no_role_nuldar_sheet_left.get_image(50, 0, 50, 75)
player_no_role_nuldar_left_3 = player_no_role_nuldar_sheet_left.get_image(100, 0, 50, 75)
player_no_role_nuldar_left_4 = player_no_role_nuldar_sheet_left.get_image(150, 0, 50, 75)
player_no_role_nuldar_sheet_right = SpriteSheet(resource_urls.player_no_role_nuldar_right_url)
player_no_role_nuldar_right_1 = player_no_role_nuldar_sheet_right.get_image(0, 0, 50, 75)
player_no_role_nuldar_right_2 = player_no_role_nuldar_sheet_right.get_image(50, 0, 50, 75)
player_no_role_nuldar_right_3 = player_no_role_nuldar_sheet_right.get_image(100, 0, 50, 75)
player_no_role_nuldar_right_4 = player_no_role_nuldar_sheet_right.get_image(150, 0, 50, 75)
# player mage amuna race
player_mage_amuna_sheet_down = SpriteSheet(resource_urls.player_mage_amuna_down_url)
player_mage_amuna_down_1 = player_mage_amuna_sheet_down.get_image(0, 0, 50, 75)
player_mage_amuna_down_2 = player_mage_amuna_sheet_down.get_image(50, 0, 50, 75)
player_mage_amuna_down_3 = player_mage_amuna_sheet_down.get_image(100, 0, 50, 75)
player_mage_amuna_down_4 = player_mage_amuna_sheet_down.get_image(150, 0, 50, 75)
player_mage_amuna_sheet_up = SpriteSheet(resource_urls.player_mage_amuna_up_url)
player_mage_amuna_up_1 = player_mage_amuna_sheet_up.get_image(0, 0, 50, 75)
player_mage_amuna_up_2 = player_mage_amuna_sheet_up.get_image(50, 0, 50, 75)
player_mage_amuna_up_3 = player_mage_amuna_sheet_up.get_image(100, 0, 50, 75)
player_mage_amuna_up_4 = player_mage_amuna_sheet_up.get_image(150, 0, 50, 75)
player_mage_amuna_sheet_left = SpriteSheet(resource_urls.player_mage_amuna_left_url)
player_mage_amuna_left_1 = player_mage_amuna_sheet_left.get_image(0, 0, 50, 75)
player_mage_amuna_left_2 = player_mage_amuna_sheet_left.get_image(50, 0, 50, 75)
player_mage_amuna_left_3 = player_mage_amuna_sheet_left.get_image(100, 0, 50, 75)
player_mage_amuna_left_4 = player_mage_amuna_sheet_left.get_image(150, 0, 50, 75)
player_mage_amuna_sheet_right = SpriteSheet(resource_urls.player_mage_amuna_right_url)
player_mage_amuna_right_1 = player_mage_amuna_sheet_right.get_image(0, 0, 50, 75)
player_mage_amuna_right_2 = player_mage_amuna_sheet_right.get_image(50, 0, 50, 75)
player_mage_amuna_right_3 = player_mage_amuna_sheet_right.get_image(100, 0, 50, 75)
player_mage_amuna_right_4 = player_mage_amuna_sheet_right.get_image(150, 0, 50, 75)
# player mage nuldar race
player_mage_nuldar_sheet_down = SpriteSheet(resource_urls.player_mage_nuldar_down_url)
player_mage_nuldar_down_1 = player_mage_nuldar_sheet_down.get_image(0, 0, 50, 75)
player_mage_nuldar_down_2 = player_mage_nuldar_sheet_down.get_image(50, 0, 50, 75)
player_mage_nuldar_down_3 = player_mage_nuldar_sheet_down.get_image(100, 0, 50, 75)
player_mage_nuldar_down_4 = player_mage_nuldar_sheet_down.get_image(150, 0, 50, 75)
player_mage_nuldar_sheet_up = SpriteSheet(resource_urls.player_mage_nuldar_up_url)
player_mage_nuldar_up_1 = player_mage_nuldar_sheet_up.get_image(0, 0, 50, 75)
player_mage_nuldar_up_2 = player_mage_nuldar_sheet_up.get_image(50, 0, 50, 75)
player_mage_nuldar_up_3 = player_mage_nuldar_sheet_up.get_image(100, 0, 50, 75)
player_mage_nuldar_up_4 = player_mage_nuldar_sheet_up.get_image(150, 0, 50, 75)
player_mage_nuldar_sheet_left = SpriteSheet(resource_urls.player_mage_nuldar_left_url)
player_mage_nuldar_left_1 = player_mage_nuldar_sheet_left.get_image(0, 0, 50, 75)
player_mage_nuldar_left_2 = player_mage_nuldar_sheet_left.get_image(50, 0, 50, 75)
player_mage_nuldar_left_3 = player_mage_nuldar_sheet_left.get_image(100, 0, 50, 75)
player_mage_nuldar_left_4 = player_mage_nuldar_sheet_left.get_image(150, 0, 50, 75)
player_mage_nuldar_sheet_right = SpriteSheet(resource_urls.player_mage_nuldar_right_url)
player_mage_nuldar_right_1 = player_mage_nuldar_sheet_right.get_image(0, 0, 50, 75)
player_mage_nuldar_right_2 = player_mage_nuldar_sheet_right.get_image(50, 0, 50, 75)
player_mage_nuldar_right_3 = player_mage_nuldar_sheet_right.get_image(100, 0, 50, 75)
player_mage_nuldar_right_4 = player_mage_nuldar_sheet_right.get_image(150, 0, 50, 75)
# player mage sorae race
player_mage_sorae_sheet_down = SpriteSheet(resource_urls.player_mage_sorae_down_url)
player_mage_sorae_down_1 = player_mage_sorae_sheet_down.get_image(0, 0, 50, 75)
player_mage_sorae_down_2 = player_mage_sorae_sheet_down.get_image(50, 0, 50, 75)
player_mage_sorae_down_3 = player_mage_sorae_sheet_down.get_image(100, 0, 50, 75)
player_mage_sorae_down_4 = player_mage_sorae_sheet_down.get_image(150, 0, 50, 75)
player_mage_sorae_sheet_up = SpriteSheet(resource_urls.player_mage_sorae_up_url)
player_mage_sorae_up_1 = player_mage_sorae_sheet_up.get_image(0, 0, 50, 75)
player_mage_sorae_up_2 = player_mage_sorae_sheet_up.get_image(50, 0, 50, 75)
player_mage_sorae_up_3 = player_mage_sorae_sheet_up.get_image(100, 0, 50, 75)
player_mage_sorae_up_4 = player_mage_sorae_sheet_up.get_image(150, 0, 50, 75)
player_mage_sorae_sheet_left = SpriteSheet(resource_urls.player_mage_sorae_left_url)
player_mage_sorae_left_1 = player_mage_sorae_sheet_left.get_image(0, 0, 50, 75)
player_mage_sorae_left_2 = player_mage_sorae_sheet_left.get_image(50, 0, 50, 75)
player_mage_sorae_left_3 = player_mage_sorae_sheet_left.get_image(100, 0, 50, 75)
player_mage_sorae_left_4 = player_mage_sorae_sheet_left.get_image(150, 0, 50, 75)
player_mage_sorae_sheet_right = SpriteSheet(resource_urls.player_mage_sorae_right_url)
player_mage_sorae_right_1 = player_mage_sorae_sheet_right.get_image(0, 0, 50, 75)
player_mage_sorae_right_2 = player_mage_sorae_sheet_right.get_image(50, 0, 50, 75)
player_mage_sorae_right_3 = player_mage_sorae_sheet_right.get_image(100, 0, 50, 75)
player_mage_sorae_right_4 = player_mage_sorae_sheet_right.get_image(150, 0, 50, 75)
# player fighter amuna race
player_fighter_amuna_sheet_down = SpriteSheet(resource_urls.player_fighter_amuna_down_url)
player_fighter_amuna_down_1 = player_fighter_amuna_sheet_down.get_image(0, 0, 50, 75)
player_fighter_amuna_down_2 = player_fighter_amuna_sheet_down.get_image(50, 0, 50, 75)
player_fighter_amuna_down_3 = player_fighter_amuna_sheet_down.get_image(100, 0, 50, 75)
player_fighter_amuna_down_4 = player_fighter_amuna_sheet_down.get_image(150, 0, 50, 75)
player_fighter_amuna_sheet_up = SpriteSheet(resource_urls.player_fighter_amuna_up_url)
player_fighter_amuna_up_1 = player_fighter_amuna_sheet_up.get_image(0, 0, 50, 75)
player_fighter_amuna_up_2 = player_fighter_amuna_sheet_up.get_image(50, 0, 50, 75)
player_fighter_amuna_up_3 = player_fighter_amuna_sheet_up.get_image(100, 0, 50, 75)
player_fighter_amuna_up_4 = player_fighter_amuna_sheet_up.get_image(150, 0, 50, 75)
player_fighter_amuna_sheet_left = SpriteSheet(resource_urls.player_fighter_amuna_left_url)
player_fighter_amuna_left_1 = player_fighter_amuna_sheet_left.get_image(0, 0, 50, 75)
player_fighter_amuna_left_2 = player_fighter_amuna_sheet_left.get_image(50, 0, 50, 75)
player_fighter_amuna_left_3 = player_fighter_amuna_sheet_left.get_image(100, 0, 50, 75)
player_fighter_amuna_left_4 = player_fighter_amuna_sheet_left.get_image(150, 0, 50, 75)
player_fighter_amuna_sheet_right = SpriteSheet(resource_urls.player_fighter_amuna_right_url)
player_fighter_amuna_right_1 = player_fighter_amuna_sheet_right.get_image(0, 0, 50, 75)
player_fighter_amuna_right_2 = player_fighter_amuna_sheet_right.get_image(50, 0, 50, 75)
player_fighter_amuna_right_3 = player_fighter_amuna_sheet_right.get_image(100, 0, 50, 75)
player_fighter_amuna_right_4 = player_fighter_amuna_sheet_right.get_image(150, 0, 50, 75)
# player fighter nuldar race
player_fighter_nuldar_sheet_down = SpriteSheet(resource_urls.player_fighter_nuldar_down_url)
player_fighter_nuldar_down_1 = player_fighter_nuldar_sheet_down.get_image(0, 0, 50, 75)
player_fighter_nuldar_down_2 = player_fighter_nuldar_sheet_down.get_image(50, 0, 50, 75)
player_fighter_nuldar_down_3 = player_fighter_nuldar_sheet_down.get_image(100, 0, 50, 75)
player_fighter_nuldar_down_4 = player_fighter_nuldar_sheet_down.get_image(150, 0, 50, 75)
player_fighter_nuldar_sheet_up = SpriteSheet(resource_urls.player_fighter_nuldar_up_url)
player_fighter_nuldar_up_1 = player_fighter_nuldar_sheet_up.get_image(0, 0, 50, 75)
player_fighter_nuldar_up_2 = player_fighter_nuldar_sheet_up.get_image(50, 0, 50, 75)
player_fighter_nuldar_up_3 = player_fighter_nuldar_sheet_up.get_image(100, 0, 50, 75)
player_fighter_nuldar_up_4 = player_fighter_nuldar_sheet_up.get_image(150, 0, 50, 75)
player_fighter_nuldar_sheet_left = SpriteSheet(resource_urls.player_fighter_nuldar_left_url)
player_fighter_nuldar_left_1 = player_fighter_nuldar_sheet_left.get_image(0, 0, 50, 75)
player_fighter_nuldar_left_2 = player_fighter_nuldar_sheet_left.get_image(50, 0, 50, 75)
player_fighter_nuldar_left_3 = player_fighter_nuldar_sheet_left.get_image(100, 0, 50, 75)
player_fighter_nuldar_left_4 = player_fighter_nuldar_sheet_left.get_image(150, 0, 50, 75)
player_fighter_nuldar_sheet_right = SpriteSheet(resource_urls.player_fighter_nuldar_right_url)
player_fighter_nuldar_right_1 = player_fighter_nuldar_sheet_right.get_image(0, 0, 50, 75)
player_fighter_nuldar_right_2 = player_fighter_nuldar_sheet_right.get_image(50, 0, 50, 75)
player_fighter_nuldar_right_3 = player_fighter_nuldar_sheet_right.get_image(100, 0, 50, 75)
player_fighter_nuldar_right_4 = player_fighter_nuldar_sheet_right.get_image(150, 0, 50, 75)
# player fighter sorae race
player_fighter_sorae_sheet_down = SpriteSheet(resource_urls.player_fighter_sorae_down_url)
player_fighter_sorae_down_1 = player_fighter_sorae_sheet_down.get_image(0, 0, 50, 75)
player_fighter_sorae_down_2 = player_fighter_sorae_sheet_down.get_image(50, 0, 50, 75)
player_fighter_sorae_down_3 = player_fighter_sorae_sheet_down.get_image(100, 0, 50, 75)
player_fighter_sorae_down_4 = player_fighter_sorae_sheet_down.get_image(150, 0, 50, 75)
player_fighter_sorae_sheet_up = SpriteSheet(resource_urls.player_fighter_sorae_up_url)
player_fighter_sorae_up_1 = player_fighter_sorae_sheet_up.get_image(0, 0, 50, 75)
player_fighter_sorae_up_2 = player_fighter_sorae_sheet_up.get_image(50, 0, 50, 75)
player_fighter_sorae_up_3 = player_fighter_sorae_sheet_up.get_image(100, 0, 50, 75)
player_fighter_sorae_up_4 = player_fighter_sorae_sheet_up.get_image(150, 0, 50, 75)
player_fighter_sorae_sheet_left = SpriteSheet(resource_urls.player_fighter_sorae_left_url)
player_fighter_sorae_left_1 = player_fighter_sorae_sheet_left.get_image(0, 0, 50, 75)
player_fighter_sorae_left_2 = player_fighter_sorae_sheet_left.get_image(50, 0, 50, 75)
player_fighter_sorae_left_3 = player_fighter_sorae_sheet_left.get_image(100, 0, 50, 75)
player_fighter_sorae_left_4 = player_fighter_sorae_sheet_left.get_image(150, 0, 50, 75)
player_fighter_sorae_sheet_right = SpriteSheet(resource_urls.player_fighter_sorae_right_url)
player_fighter_sorae_right_1 = player_fighter_sorae_sheet_right.get_image(0, 0, 50, 75)
player_fighter_sorae_right_2 = player_fighter_sorae_sheet_right.get_image(50, 0, 50, 75)
player_fighter_sorae_right_3 = player_fighter_sorae_sheet_right.get_image(100, 0, 50, 75)
player_fighter_sorae_right_4 = player_fighter_sorae_sheet_right.get_image(150, 0, 50, 75)
# player scout amuna race
player_scout_amuna_sheet_down = SpriteSheet(resource_urls.player_scout_amuna_down_url)
player_scout_amuna_down_1 = player_scout_amuna_sheet_down.get_image(0, 0, 50, 75)
player_scout_amuna_down_2 = player_scout_amuna_sheet_down.get_image(50, 0, 50, 75)
player_scout_amuna_down_3 = player_scout_amuna_sheet_down.get_image(100, 0, 50, 75)
player_scout_amuna_down_4 = player_scout_amuna_sheet_down.get_image(150, 0, 50, 75)
player_scout_amuna_sheet_up = SpriteSheet(resource_urls.player_scout_amuna_up_url)
player_scout_amuna_up_1 = player_scout_amuna_sheet_up.get_image(0, 0, 50, 75)
player_scout_amuna_up_2 = player_scout_amuna_sheet_up.get_image(50, 0, 50, 75)
player_scout_amuna_up_3 = player_scout_amuna_sheet_up.get_image(100, 0, 50, 75)
player_scout_amuna_up_4 = player_scout_amuna_sheet_up.get_image(150, 0, 50, 75)
player_scout_amuna_sheet_left = SpriteSheet(resource_urls.player_scout_amuna_left_url)
player_scout_amuna_left_1 = player_scout_amuna_sheet_left.get_image(0, 0, 50, 75)
player_scout_amuna_left_2 = player_scout_amuna_sheet_left.get_image(50, 0, 50, 75)
player_scout_amuna_left_3 = player_scout_amuna_sheet_left.get_image(100, 0, 50, 75)
player_scout_amuna_left_4 = player_scout_amuna_sheet_left.get_image(150, 0, 50, 75)
player_scout_amuna_sheet_right = SpriteSheet(resource_urls.player_scout_amuna_right_url)
player_scout_amuna_right_1 = player_scout_amuna_sheet_right.get_image(0, 0, 50, 75)
player_scout_amuna_right_2 = player_scout_amuna_sheet_right.get_image(50, 0, 50, 75)
player_scout_amuna_right_3 = player_scout_amuna_sheet_right.get_image(100, 0, 50, 75)
player_scout_amuna_right_4 = player_scout_amuna_sheet_right.get_image(150, 0, 50, 75)
# player scout nuldar race
player_scout_nuldar_sheet_down = SpriteSheet(resource_urls.player_scout_nuldar_down_url)
player_scout_nuldar_down_1 = player_scout_nuldar_sheet_down.get_image(0, 0, 50, 75)
player_scout_nuldar_down_2 = player_scout_nuldar_sheet_down.get_image(50, 0, 50, 75)
player_scout_nuldar_down_3 = player_scout_nuldar_sheet_down.get_image(100, 0, 50, 75)
player_scout_nuldar_down_4 = player_scout_nuldar_sheet_down.get_image(150, 0, 50, 75)
player_scout_nuldar_sheet_up = SpriteSheet(resource_urls.player_scout_nuldar_up_url)
player_scout_nuldar_up_1 = player_scout_nuldar_sheet_up.get_image(0, 0, 50, 75)
player_scout_nuldar_up_2 = player_scout_nuldar_sheet_up.get_image(50, 0, 50, 75)
player_scout_nuldar_up_3 = player_scout_nuldar_sheet_up.get_image(100, 0, 50, 75)
player_scout_nuldar_up_4 = player_scout_nuldar_sheet_up.get_image(150, 0, 50, 75)
player_scout_nuldar_sheet_left = SpriteSheet(resource_urls.player_scout_nuldar_left_url)
player_scout_nuldar_left_1 = player_scout_nuldar_sheet_left.get_image(0, 0, 50, 75)
player_scout_nuldar_left_2 = player_scout_nuldar_sheet_left.get_image(50, 0, 50, 75)
player_scout_nuldar_left_3 = player_scout_nuldar_sheet_left.get_image(100, 0, 50, 75)
player_scout_nuldar_left_4 = player_scout_nuldar_sheet_left.get_image(150, 0, 50, 75)
player_scout_nuldar_sheet_right = SpriteSheet(resource_urls.player_scout_nuldar_right_url)
player_scout_nuldar_right_1 = player_scout_nuldar_sheet_right.get_image(0, 0, 50, 75)
player_scout_nuldar_right_2 = player_scout_nuldar_sheet_right.get_image(50, 0, 50, 75)
player_scout_nuldar_right_3 = player_scout_nuldar_sheet_right.get_image(100, 0, 50, 75)
player_scout_nuldar_right_4 = player_scout_nuldar_sheet_right.get_image(150, 0, 50, 75)
# player scout sorae race
player_scout_sorae_sheet_down = SpriteSheet(resource_urls.player_scout_sorae_down_url)
player_scout_sorae_down_1 = player_scout_sorae_sheet_down.get_image(0, 0, 50, 75)
player_scout_sorae_down_2 = player_scout_sorae_sheet_down.get_image(50, 0, 50, 75)
player_scout_sorae_down_3 = player_scout_sorae_sheet_down.get_image(100, 0, 50, 75)
player_scout_sorae_down_4 = player_scout_sorae_sheet_down.get_image(150, 0, 50, 75)
player_scout_sorae_sheet_up = SpriteSheet(resource_urls.player_scout_sorae_up_url)
player_scout_sorae_up_1 = player_scout_sorae_sheet_up.get_image(0, 0, 50, 75)
player_scout_sorae_up_2 = player_scout_sorae_sheet_up.get_image(50, 0, 50, 75)
player_scout_sorae_up_3 = player_scout_sorae_sheet_up.get_image(100, 0, 50, 75)
player_scout_sorae_up_4 = player_scout_sorae_sheet_up.get_image(150, 0, 50, 75)
player_scout_sorae_sheet_left = SpriteSheet(resource_urls.player_scout_sorae_left_url)
player_scout_sorae_left_1 = player_scout_sorae_sheet_left.get_image(0, 0, 50, 75)
player_scout_sorae_left_2 = player_scout_sorae_sheet_left.get_image(50, 0, 50, 75)
player_scout_sorae_left_3 = player_scout_sorae_sheet_left.get_image(100, 0, 50, 75)
player_scout_sorae_left_4 = player_scout_sorae_sheet_left.get_image(150, 0, 50, 75)
player_scout_sorae_sheet_right = SpriteSheet(resource_urls.player_scout_sorae_right_url)
player_scout_sorae_right_1 = player_scout_sorae_sheet_right.get_image(0, 0, 50, 75)
player_scout_sorae_right_2 = player_scout_sorae_sheet_right.get_image(50, 0, 50, 75)
player_scout_sorae_right_3 = player_scout_sorae_sheet_right.get_image(100, 0, 50, 75)
player_scout_sorae_right_4 = player_scout_sorae_sheet_right.get_image(150, 0, 50, 75)
# player battle amuna race
player_battle_amuna_sheet = SpriteSheet(resource_urls.player_battle_amuna_url)
player_no_role_amuna_battle = player_battle_amuna_sheet.get_image(0, 0, 750, 624)
player_no_role_amuna_attack = player_battle_amuna_sheet.get_image(750, 0, 750, 624)
player_mage_amuna_battle = player_battle_amuna_sheet.get_image(1500, 0, 750, 624)
player_mage_amuna_attack = player_battle_amuna_sheet.get_image(2250, 0, 750, 624)
player_fighter_amuna_battle = player_battle_amuna_sheet.get_image(3000, 0, 750, 624)
player_fighter_amuna_attack = player_battle_amuna_sheet.get_image(3750, 0, 750, 624)
player_scout_amuna_battle = player_battle_amuna_sheet.get_image(4500, 0, 750, 624)
player_scout_amuna_attack = player_battle_amuna_sheet.get_image(5250, 0, 750, 624)
# player skills amuna race
player_skills_amuna_sheet = SpriteSheet(resource_urls.player_skills_amuna_url)
player_mage_barrier_amuna_battle = player_skills_amuna_sheet.get_image(0, 0, 750, 624)
player_mage_barrier_amuna_attack = player_skills_amuna_sheet.get_image(750, 0, 750, 624)
player_scout_sense_amuna_battle = player_skills_amuna_sheet.get_image(1500, 0, 750, 624)
player_scout_sense_amuna_attack = player_skills_amuna_sheet.get_image(2250, 0, 750, 624)
player_fighter_amuna_strike = player_skills_amuna_sheet.get_image(3000, 0, 750, 624)
# player battle sorae race
player_battle_sorae_sheet = SpriteSheet(resource_urls.player_battle_sorae_url)
player_no_role_sorae_battle = player_battle_sorae_sheet.get_image(0, 0, 750, 624)
player_no_role_sorae_attack = player_battle_sorae_sheet.get_image(750, 0, 750, 624)
player_mage_sorae_battle = player_battle_sorae_sheet.get_image(1500, 0, 750, 624)
player_mage_sorae_attack = player_battle_sorae_sheet.get_image(2250, 0, 750, 624)
player_fighter_sorae_battle = player_battle_sorae_sheet.get_image(3000, 0, 750, 624)
player_fighter_sorae_attack = player_battle_sorae_sheet.get_image(3750, 0, 750, 624)
player_scout_sorae_battle = player_battle_sorae_sheet.get_image(4500, 0, 750, 624)
player_scout_sorae_attack = player_battle_sorae_sheet.get_image(5250, 0, 750, 624)
# player skills sorae race
player_skills_sorae_sheet = SpriteSheet(resource_urls.player_skills_sorae_url)
player_mage_barrier_sorae_battle = player_skills_sorae_sheet.get_image(0, 0, 750, 624)
player_mage_barrier_sorae_attack = player_skills_sorae_sheet.get_image(750, 0, 750, 624)
player_scout_sense_sorae_battle = player_skills_sorae_sheet.get_image(1500, 0, 750, 624)
player_scout_sense_sorae_attack = player_skills_sorae_sheet.get_image(2250, 0, 750, 624)
player_fighter_sorae_strike = player_skills_sorae_sheet.get_image(3000, 0, 750, 624)
# player battle nuldar race
player_battle_nuldar_sheet = SpriteSheet(resource_urls.player_battle_nuldar_url)
player_no_role_nuldar_battle = player_battle_nuldar_sheet.get_image(0, 0, 750, 624)
player_no_role_nuldar_attack = player_battle_nuldar_sheet.get_image(750, 0, 750, 624)
player_mage_nuldar_battle = player_battle_nuldar_sheet.get_image(1500, 0, 750, 624)
player_mage_nuldar_attack = player_battle_nuldar_sheet.get_image(2250, 0, 750, 624)
player_fighter_nuldar_battle = player_battle_nuldar_sheet.get_image(3000, 0, 750, 624)
player_fighter_nuldar_attack = player_battle_nuldar_sheet.get_image(3750, 0, 750, 624)
player_scout_nuldar_battle = player_battle_nuldar_sheet.get_image(4500, 0, 750, 624)
player_scout_nuldar_attack = player_battle_nuldar_sheet.get_image(5250, 0, 750, 624)
# player skills sorae race
player_skills_nuldar_sheet = SpriteSheet(resource_urls.player_skills_nuldar_url)
player_mage_barrier_nuldar_battle = player_skills_nuldar_sheet.get_image(0, 0, 750, 624)
player_mage_barrier_nuldar_attack = player_skills_nuldar_sheet.get_image(750, 0, 750, 624)
player_scout_sense_nuldar_battle = player_skills_nuldar_sheet.get_image(1500, 0, 750, 624)
player_scout_sense_nuldar_attack = player_skills_nuldar_sheet.get_image(2250, 0, 750, 624)
player_fighter_nuldar_strike = player_skills_nuldar_sheet.get_image(3000, 0, 750, 624)
# garan npc
garan_sheet = SpriteSheet(resource_urls.garan_url)
garan_down = garan_sheet.get_image(0, 0, 40, 62)
garan_up = garan_sheet.get_image(40, 0, 40, 62)
garan_left = garan_sheet.get_image(80, 0, 40, 62)
garan_right = garan_sheet.get_image(120, 0, 40, 62)
# maurelle npc
maurelle_sheet = SpriteSheet(resource_urls.maurelle_url)
maurelle_down = maurelle_sheet.get_image(0, 0, 40, 62)
maurelle_up = maurelle_sheet.get_image(40, 0, 40, 62)
maurelle_left = maurelle_sheet.get_image(80, 0, 40, 62)
maurelle_right = maurelle_sheet.get_image(120, 0, 40, 62)
# guard npc
guard_sheet = SpriteSheet(resource_urls.guard_url)
guard_down = guard_sheet.get_image(0, 0, 50, 75)
guard_up = guard_sheet.get_image(50, 0, 50, 75)
guard_left = guard_sheet.get_image(100, 0, 50, 75)
guard_right = guard_sheet.get_image(150, 0, 50, 75)
# npc interactions
npc_interactions_sheet = SpriteSheet(resource_urls.npc_interactions_url)
garan_interaction = npc_interactions_sheet.get_image(0, 0, 200, 260)
maurelle_interaction = npc_interactions_sheet.get_image(200, 0, 200, 260)
guard_interaction = npc_interactions_sheet.get_image(400, 0, 200, 260)
# enemies
enemies_sheet = SpriteSheet(resource_urls.enemies_url)
snake = enemies_sheet.get_image(0, 0, 50, 50)
ghoul = enemies_sheet.get_image(50, 0, 50, 50)
# enemies battle
enemies_battle_sheet = SpriteSheet(resource_urls.enemies_battle_url)
snake_battle = enemies_battle_sheet.get_image(0, 0, 300, 250)
snake_attack = enemies_battle_sheet.get_image(300, 0, 300, 250)
ghoul_battle = enemies_battle_sheet.get_image(600, 0, 300, 250)
ghoul_attack = enemies_battle_sheet.get_image(900, 0, 300, 250)
# amuna buildings
amuna_buildings_sheet = SpriteSheet(resource_urls.amuna_buildings_url)
amuna_academia_building = amuna_buildings_sheet.get_image(0, 0, 100, 100)
amuna_inn_building = amuna_buildings_sheet.get_image(100, 0, 100, 100)
amuna_shop_building = amuna_buildings_sheet.get_image(200, 0, 100, 100)
# nascent gate
nascent_gate_sheet = SpriteSheet(resource_urls.nascent_gate_url)
nascent_gate_closed = nascent_gate_sheet.get_image(0, 0, 178, 120)
nascent_gate_open = nascent_gate_sheet.get_image(178, 0, 178, 120)
# items
items_sheet = SpriteSheet(resource_urls.items_url)
health_pot_img = items_sheet.get_image(0, 0, 50, 50)
energy_pot_img = items_sheet.get_image(50, 0, 50, 50)
basic_robes_img = items_sheet.get_image(100, 0, 50, 50)
basic_armor_img = items_sheet.get_image(150, 0, 50, 50)
basic_tunic_img = items_sheet.get_image(200, 0, 50, 50)
basic_staff_img = items_sheet.get_image(250, 0, 50, 50)
basic_sword_img = items_sheet.get_image(300, 0, 50, 50)
basic_bow_img = items_sheet.get_image(350, 0, 50, 50)
bone_dust_img = items_sheet.get_image(400, 0, 50, 50)
shiny_rock_img = items_sheet.get_image(450, 0, 50, 50)
temp_img = items_sheet.get_image(500, 0, 50, 50)
# player info windows
player_info_sheet = SpriteSheet(resource_urls.player_info_url)
character_window_img = player_info_sheet.get_image(0, 0, 500, 525)
journal_window_img = player_info_sheet.get_image(500, 0, 500, 525)
# books
books_sheet = SpriteSheet(resource_urls.books_url)
mage_book_img = books_sheet.get_image(0, 0, 700, 525)
fighter_book_img = books_sheet.get_image(700, 0, 700, 525)
scout_book_img = books_sheet.get_image(1400, 0, 700, 525)
# start screen buttons
start_button_sheet = SpriteSheet(resource_urls.start_buttons_url)
new_game_img = start_button_sheet.get_image(0, 0, 384, 75)
continue_img = start_button_sheet.get_image(385, 0, 384, 75)
# race select buttons
race_select_button_sheet = SpriteSheet(resource_urls.race_select_buttons_url)
amuna_button_img = race_select_button_sheet.get_image(0, 0, 384, 75)
nuldar_button_img = race_select_button_sheet.get_image(385, 0, 384, 75)
sorae_button_img = race_select_button_sheet.get_image(770, 0, 384, 75)
# main buttons
buttons_sheet = SpriteSheet(resource_urls.buttons_url)
character_button_img = buttons_sheet.get_image(0, 0, 100, 50)
journal_button_img = buttons_sheet.get_image(100, 0, 100, 50)
buy_button_img = buttons_sheet.get_image(200, 0, 100, 50)
rest_button_img = buttons_sheet.get_image(300, 0, 100, 50)
quest_button_img = buttons_sheet.get_image(400, 0, 100, 50)
leave_button_img = buttons_sheet.get_image(500, 0, 100, 50)
accept_button_img = buttons_sheet.get_image(600, 0, 100, 50)
decline_button_img = buttons_sheet.get_image(700, 0, 100, 50)
yes_button_img = buttons_sheet.get_image(800, 0, 100, 50)
no_button_img = buttons_sheet.get_image(900, 0, 100, 50)
# attack buttons
attack_buttons_sheet = SpriteSheet(resource_urls.attack_buttons_url)
mage_attack_button_img = attack_buttons_sheet.get_image(0, 0, 60, 60)
fighter_attack_button_img = attack_buttons_sheet.get_image(60, 0, 60, 60)
scout_attack_button_img = attack_buttons_sheet.get_image(120, 0, 60, 60)
no_role_attack_button_img = attack_buttons_sheet.get_image(180, 0, 60, 60)
# skill buttons
skill_buttons_sheet = SpriteSheet(resource_urls.skill_buttons_url)
barrier_button_img = skill_buttons_sheet.get_image(0, 0, 60, 60)
strike_button_img = skill_buttons_sheet.get_image(60, 0, 60, 60)
sense_button_img = skill_buttons_sheet.get_image(120, 0, 60, 60)
# game function buttons
game_function_buttons_sheet = SpriteSheet(resource_urls.game_play_function_buttons_url)
save_button_img = game_function_buttons_sheet.get_image(0, 0, 100, 25)
hearth_button_img = game_function_buttons_sheet.get_image(100, 0, 100, 25)
# quest windows
quest_windows_sheet = SpriteSheet(resource_urls.quest_windows_url)
garan_quest = quest_windows_sheet.get_image(0, 0, 500, 525)
maurelle_quest = quest_windows_sheet.get_image(500, 0, 500, 525)
guard_quest = quest_windows_sheet.get_image(1000, 0, 500, 525)
# quest stars
quest_stars_sheet = SpriteSheet(resource_urls.quest_stars_url)
quest_start_star = quest_stars_sheet.get_image(0, 0, 50, 50)
quest_progress_star = quest_stars_sheet.get_image(50, 0, 50, 50)
quest_complete_star = quest_stars_sheet.get_image(100, 0, 50, 50)
# pop up notifications
popups_sheet = SpriteSheet(resource_urls.popups_url)
gear_popup = popups_sheet.get_image(0, 0, 400, 200)
health_popup = popups_sheet.get_image(400, 0, 400, 200)
knowledge_popup = popups_sheet.get_image(800, 0, 400, 200)
save_popup = popups_sheet.get_image(1200, 0, 400, 200)
save_not_found = popups_sheet.get_image(1600, 0, 400, 200)
# heath bars
hp_sheet = SpriteSheet(resource_urls.hp_url)
hp_0 = hp_sheet.get_image(0, 0, 305, 19); hp_1 = hp_sheet.get_image(305, 0, 305, 19)
hp_2 = hp_sheet.get_image(610, 0, 305, 19); hp_3 = hp_sheet.get_image(915, 0, 305, 19)
hp_4 = hp_sheet.get_image(1220, 0, 305, 19); hp_5 = hp_sheet.get_image(1525, 0, 305, 19)
hp_6 = hp_sheet.get_image(1830, 0, 305, 19); hp_7 = hp_sheet.get_image(2135, 0, 305, 19)
hp_8 = hp_sheet.get_image(2440, 0, 305, 19); hp_9 = hp_sheet.get_image(2745, 0, 305, 19)
hp_10 = hp_sheet.get_image(0, 19, 305, 19); hp_11 = hp_sheet.get_image(305, 19, 305, 19)
hp_12 = hp_sheet.get_image(610, 19, 305, 19); hp_13 = hp_sheet.get_image(915, 19, 305, 19)
hp_14 = hp_sheet.get_image(1220, 19, 305, 19); hp_15 = hp_sheet.get_image(1525, 19, 305, 19)
hp_16 = hp_sheet.get_image(1830, 19, 305, 19); hp_17 = hp_sheet.get_image(2135, 19, 305, 19)
hp_18 = hp_sheet.get_image(2440, 19, 305, 19); hp_19 = hp_sheet.get_image(2745, 19, 305, 19)
hp_20 = hp_sheet.get_image(0, 38, 305, 19); hp_21 = hp_sheet.get_image(305, 38, 305, 19)
hp_22 = hp_sheet.get_image(610, 38, 305, 19); hp_23 = hp_sheet.get_image(915, 38, 305, 19)
hp_24 = hp_sheet.get_image(1220, 38, 305, 19); hp_25 = hp_sheet.get_image(1525, 38, 305, 19)
hp_26 = hp_sheet.get_image(1830, 38, 305, 19); hp_27 = hp_sheet.get_image(2135, 38, 305, 19)
hp_28 = hp_sheet.get_image(2440, 38, 305, 19); hp_29 = hp_sheet.get_image(2745, 38, 305, 19)
hp_30 = hp_sheet.get_image(0, 57, 305, 19); hp_31 = hp_sheet.get_image(305, 57, 305, 19)
hp_32 = hp_sheet.get_image(610, 57, 305, 19); hp_33 = hp_sheet.get_image(915, 57, 305, 19)
hp_34 = hp_sheet.get_image(1220, 57, 305, 19); hp_35 = hp_sheet.get_image(1525, 57, 305, 19)
hp_36 = hp_sheet.get_image(1830, 57, 305, 19); hp_37 = hp_sheet.get_image(2135, 57, 305, 19)
hp_38 = hp_sheet.get_image(2440, 57, 305, 19); hp_39 = hp_sheet.get_image(2745, 57, 305, 19)
hp_40 = hp_sheet.get_image(0, 76, 305, 19); hp_41 = hp_sheet.get_image(305, 76, 305, 19)
hp_42 = hp_sheet.get_image(610, 76, 305, 19); hp_43 = hp_sheet.get_image(915, 76, 305, 19)
hp_44 = hp_sheet.get_image(1220, 76, 305, 19); hp_45 = hp_sheet.get_image(1525, 76, 305, 19)
hp_46 = hp_sheet.get_image(1830, 76, 305, 19); hp_47 = hp_sheet.get_image(2135, 76, 305, 19)
hp_48 = hp_sheet.get_image(2440, 76, 305, 19); hp_49 = hp_sheet.get_image(2745, 76, 305, 19)
hp_50 = hp_sheet.get_image(0, 95, 305, 19); hp_51 = hp_sheet.get_image(305, 95, 305, 19)
hp_52 = hp_sheet.get_image(610, 95, 305, 19); hp_53 = hp_sheet.get_image(915, 95, 305, 19)
hp_54 = hp_sheet.get_image(1220, 95, 305, 19); hp_55 = hp_sheet.get_image(1525, 95, 305, 19)
hp_56 = hp_sheet.get_image(1830, 95, 305, 19); hp_57 = hp_sheet.get_image(2135, 95, 305, 19)
hp_58 = hp_sheet.get_image(2440, 95, 305, 19); hp_59 = hp_sheet.get_image(2745, 95, 305, 19)
hp_60 = hp_sheet.get_image(0, 114, 305, 19); hp_61 = hp_sheet.get_image(305, 114, 305, 19)
hp_62 = hp_sheet.get_image(610, 114, 305, 19); hp_63 = hp_sheet.get_image(915, 114, 305, 19)
hp_64 = hp_sheet.get_image(1220, 114, 305, 19); hp_65 = hp_sheet.get_image(1525, 114, 305, 19)
hp_66 = hp_sheet.get_image(1830, 114, 305, 19); hp_67 = hp_sheet.get_image(2135, 114, 305, 19)
hp_68 = hp_sheet.get_image(2440, 114, 305, 19); hp_69 = hp_sheet.get_image(2745, 114, 305, 19)
hp_70 = hp_sheet.get_image(0, 133, 305, 19); hp_71 = hp_sheet.get_image(305, 133, 305, 19)
hp_72 = hp_sheet.get_image(610, 133, 305, 19); hp_73 = hp_sheet.get_image(915, 133, 305, 19)
hp_74 = hp_sheet.get_image(1220, 133, 305, 19); hp_75 = hp_sheet.get_image(1525, 133, 305, 19)
hp_76 = hp_sheet.get_image(1830, 133, 305, 19); hp_77 = hp_sheet.get_image(2135, 133, 305, 19)
hp_78 = hp_sheet.get_image(2440, 133, 305, 19); hp_79 = hp_sheet.get_image(2745, 133, 305, 19)
hp_80 = hp_sheet.get_image(0, 152, 305, 19); hp_81 = hp_sheet.get_image(305, 152, 305, 19)
hp_82 = hp_sheet.get_image(610, 152, 305, 19); hp_83 = hp_sheet.get_image(915, 152, 305, 19)
hp_84 = hp_sheet.get_image(1220, 152, 305, 19); hp_85 = hp_sheet.get_image(1525, 152, 305, 19)
hp_86 = hp_sheet.get_image(1830, 152, 305, 19); hp_87 = hp_sheet.get_image(2135, 152, 305, 19)
hp_88 = hp_sheet.get_image(2440, 152, 305, 19); hp_89 = hp_sheet.get_image(2745, 152, 305, 19)
hp_90 = hp_sheet.get_image(0, 171, 305, 19); hp_91 = hp_sheet.get_image(305, 171, 305, 19)
hp_92 = hp_sheet.get_image(610, 171, 305, 19); hp_93 = hp_sheet.get_image(915, 171, 305, 19)
hp_94 = hp_sheet.get_image(1220, 171, 305, 19); hp_95 = hp_sheet.get_image(1525, 171, 305, 19)
hp_96 = hp_sheet.get_image(1830, 171, 305, 19); hp_97 = hp_sheet.get_image(2135, 171, 305, 19)
hp_98 = hp_sheet.get_image(2440, 171, 305, 19); hp_99 = hp_sheet.get_image(2745, 171, 305, 19)
hp_100 = hp_sheet.get_image(0, 190, 305, 19)
# energy bars
en_sheet = SpriteSheet(resource_urls.en_url)
en_0 = en_sheet.get_image(0, 0, 305, 19); en_1 = en_sheet.get_image(305, 0, 305, 19)
en_2 = en_sheet.get_image(610, 0, 305, 19); en_3 = en_sheet.get_image(915, 0, 305, 19)
en_4 = en_sheet.get_image(1220, 0, 305, 19); en_5 = en_sheet.get_image(1525, 0, 305, 19)
en_6 = en_sheet.get_image(1830, 0, 305, 19); en_7 = en_sheet.get_image(2135, 0, 305, 19)
en_8 = en_sheet.get_image(2440, 0, 305, 19); en_9 = en_sheet.get_image(2745, 0, 305, 19)
en_10 = en_sheet.get_image(0, 19, 305, 19); en_11 = en_sheet.get_image(305, 19, 305, 19)
en_12 = en_sheet.get_image(610, 19, 305, 19); en_13 = en_sheet.get_image(915, 19, 305, 19)
en_14 = en_sheet.get_image(1220, 19, 305, 19); en_15 = en_sheet.get_image(1525, 19, 305, 19)
en_16 = en_sheet.get_image(1830, 19, 305, 19); en_17 = en_sheet.get_image(2135, 19, 305, 19)
en_18 = en_sheet.get_image(2440, 19, 305, 19); en_19 = en_sheet.get_image(2745, 19, 305, 19)
en_20 = en_sheet.get_image(0, 38, 305, 19); en_21 = en_sheet.get_image(305, 38, 305, 19)
en_22 = en_sheet.get_image(610, 38, 305, 19); en_23 = en_sheet.get_image(915, 38, 305, 19)
en_24 = en_sheet.get_image(1220, 38, 305, 19); en_25 = en_sheet.get_image(1525, 38, 305, 19)
en_26 = en_sheet.get_image(1830, 38, 305, 19); en_27 = en_sheet.get_image(2135, 38, 305, 19)
en_28 = en_sheet.get_image(2440, 38, 305, 19); en_29 = en_sheet.get_image(2745, 38, 305, 19)
en_30 = en_sheet.get_image(0, 57, 305, 19); en_31 = en_sheet.get_image(305, 57, 305, 19)
en_32 = en_sheet.get_image(610, 57, 305, 19); en_33 = en_sheet.get_image(915, 57, 305, 19)
en_34 = en_sheet.get_image(1220, 57, 305, 19); en_35 = en_sheet.get_image(1525, 57, 305, 19)
en_36 = en_sheet.get_image(1830, 57, 305, 19); en_37 = en_sheet.get_image(2135, 57, 305, 19)
en_38 = en_sheet.get_image(2440, 57, 305, 19); en_39 = en_sheet.get_image(2745, 57, 305, 19)
en_40 = en_sheet.get_image(0, 76, 305, 19); en_41 = en_sheet.get_image(305, 76, 305, 19)
en_42 = en_sheet.get_image(610, 76, 305, 19); en_43 = en_sheet.get_image(915, 76, 305, 19)
en_44 = en_sheet.get_image(1220, 76, 305, 19); en_45 = en_sheet.get_image(1525, 76, 305, 19)
en_46 = en_sheet.get_image(1830, 76, 305, 19); en_47 = en_sheet.get_image(2135, 76, 305, 19)
en_48 = en_sheet.get_image(2440, 76, 305, 19); en_49 = en_sheet.get_image(2745, 76, 305, 19)
en_50 = en_sheet.get_image(0, 95, 305, 19); en_51 = en_sheet.get_image(305, 95, 305, 19)
en_52 = en_sheet.get_image(610, 95, 305, 19); en_53 = en_sheet.get_image(915, 95, 305, 19)
en_54 = en_sheet.get_image(1220, 95, 305, 19); en_55 = en_sheet.get_image(1525, 95, 305, 19)
en_56 = en_sheet.get_image(1830, 95, 305, 19); en_57 = en_sheet.get_image(2135, 95, 305, 19)
en_58 = en_sheet.get_image(2440, 95, 305, 19); en_59 = en_sheet.get_image(2745, 95, 305, 19)
en_60 = en_sheet.get_image(0, 114, 305, 19); en_61 = en_sheet.get_image(305, 114, 305, 19)
en_62 = en_sheet.get_image(610, 114, 305, 19); en_63 = en_sheet.get_image(915, 114, 305, 19)
en_64 = en_sheet.get_image(1220, 114, 305, 19); en_65 = en_sheet.get_image(1525, 114, 305, 19)
en_66 = en_sheet.get_image(1830, 114, 305, 19); en_67 = en_sheet.get_image(2135, 114, 305, 19)
en_68 = en_sheet.get_image(2440, 114, 305, 19); en_69 = en_sheet.get_image(2745, 114, 305, 19)
en_70 = en_sheet.get_image(0, 133, 305, 19); en_71 = en_sheet.get_image(305, 133, 305, 19)
en_72 = en_sheet.get_image(610, 133, 305, 19); en_73 = en_sheet.get_image(915, 133, 305, 19)
en_74 = en_sheet.get_image(1220, 133, 305, 19); en_75 = en_sheet.get_image(1525, 133, 305, 19)
en_76 = en_sheet.get_image(1830, 133, 305, 19); en_77 = en_sheet.get_image(2135, 133, 305, 19)
en_78 = en_sheet.get_image(2440, 133, 305, 19); en_79 = en_sheet.get_image(2745, 133, 305, 19)
en_80 = en_sheet.get_image(0, 152, 305, 19); en_81 = en_sheet.get_image(305, 152, 305, 19)
en_82 = en_sheet.get_image(610, 152, 305, 19); en_83 = en_sheet.get_image(915, 152, 305, 19)
en_84 = en_sheet.get_image(1220, 152, 305, 19); en_85 = en_sheet.get_image(1525, 152, 305, 19)
en_86 = en_sheet.get_image(1830, 152, 305, 19); en_87 = en_sheet.get_image(2135, 152, 305, 19)
en_88 = en_sheet.get_image(2440, 152, 305, 19); en_89 = en_sheet.get_image(2745, 152, 305, 19)
en_90 = en_sheet.get_image(0, 171, 305, 19); en_91 = en_sheet.get_image(305, 171, 305, 19)
en_92 = en_sheet.get_image(610, 171, 305, 19); en_93 = en_sheet.get_image(915, 171, 305, 19)
en_94 = en_sheet.get_image(1220, 171, 305, 19); en_95 = en_sheet.get_image(1525, 171, 305, 19)
en_96 = en_sheet.get_image(1830, 171, 305, 19); en_97 = en_sheet.get_image(2135, 171, 305, 19)
en_98 = en_sheet.get_image(2440, 171, 305, 19); en_99 = en_sheet.get_image(2745, 171, 305, 19)
en_100 = en_sheet.get_image(0, 190, 305, 19)
# xp bars
xp_sheet = SpriteSheet(resource_urls.xp_url)
xp_0 = xp_sheet.get_image(0, 0, 305, 19); xp_1 = xp_sheet.get_image(305, 0, 305, 19)
xp_2 = xp_sheet.get_image(610, 0, 305, 19); xp_3 = xp_sheet.get_image(915, 0, 305, 19)
xp_4 = xp_sheet.get_image(1220, 0, 305, 19); xp_5 = xp_sheet.get_image(1525, 0, 305, 19)
xp_6 = xp_sheet.get_image(1830, 0, 305, 19); xp_7 = xp_sheet.get_image(2135, 0, 305, 19)
xp_8 = xp_sheet.get_image(2440, 0, 305, 19); xp_9 = xp_sheet.get_image(2745, 0, 305, 19)
xp_10 = xp_sheet.get_image(0, 19, 305, 19); xp_11 = xp_sheet.get_image(305, 19, 305, 19)
xp_12 = xp_sheet.get_image(610, 19, 305, 19); xp_13 = xp_sheet.get_image(915, 19, 305, 19)
xp_14 = xp_sheet.get_image(1220, 19, 305, 19); xp_15 = xp_sheet.get_image(1525, 19, 305, 19)
xp_16 = xp_sheet.get_image(1830, 19, 305, 19); xp_17 = xp_sheet.get_image(2135, 19, 305, 19)
xp_18 = xp_sheet.get_image(2440, 19, 305, 19); xp_19 = xp_sheet.get_image(2745, 19, 305, 19)
xp_20 = xp_sheet.get_image(0, 38, 305, 19); xp_21 = xp_sheet.get_image(305, 38, 305, 19)
xp_22 = xp_sheet.get_image(610, 38, 305, 19); xp_23 = xp_sheet.get_image(915, 38, 305, 19)
xp_24 = xp_sheet.get_image(1220, 38, 305, 19); xp_25 = xp_sheet.get_image(1525, 38, 305, 19)
xp_26 = xp_sheet.get_image(1830, 38, 305, 19); xp_27 = xp_sheet.get_image(2135, 38, 305, 19)
xp_28 = xp_sheet.get_image(2440, 38, 305, 19); xp_29 = xp_sheet.get_image(2745, 38, 305, 19)
xp_30 = xp_sheet.get_image(0, 57, 305, 19); xp_31 = xp_sheet.get_image(305, 57, 305, 19)
xp_32 = xp_sheet.get_image(610, 57, 305, 19); xp_33 = xp_sheet.get_image(915, 57, 305, 19)
xp_34 = xp_sheet.get_image(1220, 57, 305, 19); xp_35 = xp_sheet.get_image(1525, 57, 305, 19)
xp_36 = xp_sheet.get_image(1830, 57, 305, 19); xp_37 = xp_sheet.get_image(2135, 57, 305, 19)
xp_38 = xp_sheet.get_image(2440, 57, 305, 19); xp_39 = xp_sheet.get_image(2745, 57, 305, 19)
xp_40 = xp_sheet.get_image(0, 76, 305, 19); xp_41 = xp_sheet.get_image(305, 76, 305, 19)
xp_42 = xp_sheet.get_image(610, 76, 305, 19); xp_43 = xp_sheet.get_image(915, 76, 305, 19)
xp_44 = xp_sheet.get_image(1220, 76, 305, 19); xp_45 = xp_sheet.get_image(1525, 76, 305, 19)
xp_46 = xp_sheet.get_image(1830, 76, 305, 19); xp_47 = xp_sheet.get_image(2135, 76, 305, 19)
xp_48 = xp_sheet.get_image(2440, 76, 305, 19); xp_49 = xp_sheet.get_image(2745, 76, 305, 19)
xp_50 = xp_sheet.get_image(0, 95, 305, 19); xp_51 = xp_sheet.get_image(305, 95, 305, 19)
xp_52 = xp_sheet.get_image(610, 95, 305, 19); xp_53 = xp_sheet.get_image(915, 95, 305, 19)
xp_54 = xp_sheet.get_image(1220, 95, 305, 19); xp_55 = xp_sheet.get_image(1525, 95, 305, 19)
xp_56 = xp_sheet.get_image(1830, 95, 305, 19); xp_57 = xp_sheet.get_image(2135, 95, 305, 19)
xp_58 = xp_sheet.get_image(2440, 95, 305, 19); xp_59 = xp_sheet.get_image(2745, 95, 305, 19)
xp_60 = xp_sheet.get_image(0, 114, 305, 19); xp_61 = xp_sheet.get_image(305, 114, 305, 19)
xp_62 = xp_sheet.get_image(610, 114, 305, 19); xp_63 = xp_sheet.get_image(915, 114, 305, 19)
xp_64 = xp_sheet.get_image(1220, 114, 305, 19); xp_65 = xp_sheet.get_image(1525, 114, 305, 19)
xp_66 = xp_sheet.get_image(1830, 114, 305, 19); xp_67 = xp_sheet.get_image(2135, 114, 305, 19)
xp_68 = xp_sheet.get_image(2440, 114, 305, 19); xp_69 = xp_sheet.get_image(2745, 114, 305, 19)
xp_70 = xp_sheet.get_image(0, 133, 305, 19); xp_71 = xp_sheet.get_image(305, 133, 305, 19)
xp_72 = xp_sheet.get_image(610, 133, 305, 19); xp_73 = xp_sheet.get_image(915, 133, 305, 19)
xp_74 = xp_sheet.get_image(1220, 133, 305, 19); xp_75 = xp_sheet.get_image(1525, 133, 305, 19)
xp_76 = xp_sheet.get_image(1830, 133, 305, 19); xp_77 = xp_sheet.get_image(2135, 133, 305, 19)
xp_78 = xp_sheet.get_image(2440, 133, 305, 19); xp_79 = xp_sheet.get_image(2745, 133, 305, 19)
xp_80 = xp_sheet.get_image(0, 152, 305, 19); xp_81 = xp_sheet.get_image(305, 152, 305, 19)
xp_82 = xp_sheet.get_image(610, 152, 305, 19); xp_83 = xp_sheet.get_image(915, 152, 305, 19)
xp_84 = xp_sheet.get_image(1220, 152, 305, 19); xp_85 = xp_sheet.get_image(1525, 152, 305, 19)
xp_86 = xp_sheet.get_image(1830, 152, 305, 19); xp_87 = xp_sheet.get_image(2135, 152, 305, 19)
xp_88 = xp_sheet.get_image(2440, 152, 305, 19); xp_89 = xp_sheet.get_image(2745, 152, 305, 19)
xp_90 = xp_sheet.get_image(0, 171, 305, 19); xp_91 = xp_sheet.get_image(305, 171, 305, 19)
xp_92 = xp_sheet.get_image(610, 171, 305, 19); xp_93 = xp_sheet.get_image(915, 171, 305, 19)
xp_94 = xp_sheet.get_image(1220, 171, 305, 19); xp_95 = xp_sheet.get_image(1525, 171, 305, 19)
xp_96 = xp_sheet.get_image(1830, 171, 305, 19); xp_97 = xp_sheet.get_image(2135, 171, 305, 19)
xp_98 = xp_sheet.get_image(2440, 171, 305, 19); xp_99 = xp_sheet.get_image(2745, 171, 305, 19)
xp_100 = xp_sheet.get_image(0, 190, 305, 19)

# creating objects from defined classes --------------------------------------------------------------------------------
# display notifications to user
knowledge_academia = Notification("knowledge academia notification", False, 510, 365, knowledge_popup)
rest_recover = Notification("rest recover", False, 510, 365, health_popup)
shop_gear = Notification("shop gear", False, 510, 365, gear_popup)
save_check = Notification("save check", False, 510, 365, save_popup)
# window that notifies player if a save file isn't found on start screen
save_absent = Notification("save absent", False, 640, 574, save_not_found)
# inventory items
health_potion = Item("health potion", "potion", 200, 200, health_pot_img)
energy_potion = Item("energy potion", "potion", 200, 200, energy_pot_img)
shiny_rock = Item("shiny rock", "rock", 200, 200, shiny_rock_img)
bone_dust = Item("bone dust", "dust", 200, 200, bone_dust_img)
# starter equipment
basic_staff = Item("basic staff", "mage", 200, 200, basic_staff_img)
basic_sword = Item("basic sword", "fighter", 200, 200, basic_sword_img)
basic_bow = Item("basic bow", "scout", 200, 200, basic_bow_img)
basic_robes = Item("basic robes", "mage", 200, 200, basic_robes_img)
basic_armor = Item("basic armor", "fighter", 200, 200, basic_armor_img)
basic_tunic = Item("basic tunic", "scout", 200, 200, basic_tunic_img)
# character selection screen display characters
amuna_character = UiElement("amuna character", 640, 360, amuna_character_img)
nuldar_character = UiElement("nuldar character", 640, 360, nuldar_character_img)
sorae_character = UiElement("sorae character", 640, 360, sorae_character_img)

# default player character
player = Player("stan", "amuna", "",  # name, race, role
                [health_potion, energy_potion],  # inventory
                {"weapon": "", "chest": ""},  # equipment ('type', 'name')
                # current quests, quest progress (x/4), quest status (quest: done)
                {"sneaky snakes": "Speak to Garan to start this quest.",
                 "village repairs": "Speak to Maurelle to start this quest.",
                 "ghouled again": "Speak to the gate Guard to start this quest.", "": ""},
                {"sneaky snakes": 0, "village repairs": 0, "ghouled again": 0},  # quest progress (x/4)
                {"sneaky snakes": False, "village repairs": False, "ghouled again": False},  # quest status
                {"sneaky snakes": False, "village repairs": False, "ghouled again": False},  # quest complete
                {"mage": 60, "fighter": 60, "scout": 60},  # role knowledge ('role', 'amount')
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # mage skills
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # fighter skills
                {"skill 2": "", "skill 3": "", "skill 4": ""},  # scout skills
                1, 0, 100, 100,  # lvl, exp, health, energy
                True, 20, {"amuna": 0, "nuldar": 0, "sorae": 0},  # alive, rupees, reputation
                "", 0, 0)  # zone, defence, offense, image

# npcs: name, gender, race, role, dialog, quest, quest_description, x_coordinate, y_coordinate
#                  alive_status, quest_complete, items, gift, image
npc_garan = NPC("garan", "male", "amuna", "rogue", "It's dangerous to go alone.", "Stupid Snakes", "", 210, 430,
                True, False, ["Items"], False, garan_down)
npc_maurelle = NPC("maurelle", "female", "amuna", "mage", "We need help!", "Village Repairs", "", 760, 520,
                   True, False, ["Items"], False, maurelle_down)
npc_guard = NPC("guard", "male", "amuna", "fighter", "Another day.", "Ghouled Again", "", 430, 120,
                True, False, ["Items"], False, guard_down)
npc_amuna_shopkeeper = Shopkeeper("amuna shopkeeper", "amuna", [
    Item("health potion", "potion", 200, 200, health_pot_img),
    Item("energy potion", "potion", 200, 200, energy_pot_img),
    Item("basic staff", "mage", 200, 200, basic_staff_img),
    Item("basic sword", "fighter", 200, 200, basic_sword_img),
    Item("basic bow", "scout", 200, 200, basic_bow_img),
    Item("basic robes", "mage", 200, 200, basic_robes_img),
    Item("basic armor", "fighter", 200, 200, basic_armor_img),
    Item("basic tunic", "scout", 200, 200, basic_tunic_img)])
npc_garan_interaction = UiElement("garan interaction", 650, 350, garan_interaction)
npc_maurelle_interaction = UiElement("maurelle interaction", 650, 350, maurelle_interaction)
npc_guard_interaction = UiElement("guard interaction", 650, 350, guard_interaction)
# enemies: kind, health, energy, level, x_coordinate, y_coordinate, alive_status, items, image, color, health bar
snake_1 = Enemy("snake", "snake", 100, 100, 1, 80, 130, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100))
snake_2 = Enemy("snake", "snake", 100, 100, 2, 285, 150, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100))
snake_3 = Enemy("snake", "snake", 100, 100, 1, 80, 230, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100))
snake_4 = Enemy("snake", "snake", 100, 100, 2, 285, 250, True,
                Item("shiny rock", "rock", 200, 200, shiny_rock_img), snake,
                UiElement("snake hp bar", 700, 90, hp_100))
ghoul_low_1 = Enemy("ghoul", "ghoul", 100, 100, 4, 665, 180, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100))
ghoul_low_2 = Enemy("ghoul", "ghoul", 100, 100, 5, 800, 130, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100))
ghoul_low_3 = Enemy("ghoul", "ghoul", 100, 100, 3, 760, 240, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100))
ghoul_low_4 = Enemy("ghoul", "ghoul", 100, 100, 4, 890, 205, True,
                    Item("bone dust", "dust", 200, 200, bone_dust_img), ghoul,
                    UiElement("ghoul hp bar", 700, 90, hp_100))
# environmental objects: name, model, x_coordinate, y_coordinate, gathered, image
pine_tree_1 = Tree("tree", "pine tree", 80, 445, False, pygame.image.load(resource_urls.pine_tree).convert())
pine_tree_2 = Tree("tree", "pine tree", 260, 590, False, pygame.image.load(resource_urls.pine_tree).convert())
pine_tree_3 = Tree("tree", "pine tree", 340, 400, False, pygame.image.load(resource_urls.pine_tree).convert())
# buildings: name, model, x_coordinate, y_coordinate, image, color
seldon_inn = Building("inn", "seldon inn", 635, 600, amuna_inn_building)
seldon_shop = Building("shop", "seldon shop", 665, 400, amuna_shop_building)
seldon_academia = Building("academia", "seldon academia", 875, 440, amuna_academia_building)
seldon_hearth = Building("hearth", "seldon hearth", 860, 595, pygame.image.load(resource_urls.hearth_stone).convert())
rohir_gate = Building("gate", "rohir gate", 525, 40, pygame.image.load(resource_urls.rohir_gate).convert())
nascent_gate = Building("gate", "nascent gate", 418, 262, nascent_gate_closed)
# ui elements: name, x_coordinate, y_coordinate, image, color, update flag
character_button = UiElement("character button", 860, 680, character_button_img)
journal_button = UiElement("journal button", 970, 680, journal_button_img)
# start screen elements
new_game_button = UiElement("new game button", 640, 342, new_game_img)
continue_button = UiElement("continue button", 640, 425, continue_img)
amuna_button = UiElement("amuna button", 100, 255, amuna_button_img)
nuldar_button = UiElement("nuldar button", 100, 350, nuldar_button_img)
sorae_button = UiElement("sorae button", 100, 445, sorae_button_img)
character_select_overlay = UiElement("character select overlay", 640, 365,
                                     pygame.image.load(resource_urls.character_select_overlay_url).convert())
amuna_select_overlay = UiElement("amuna select overlay", 1140, 305, amuna_overlay_img)
nuldar_select_overlay = UiElement("nuldar select overlay", 1140, 305, nuldar_overlay_img)
sorae_select_overlay = UiElement("sorae select overlay", 1140, 305, sorae_overlay_img)
start_button = UiElement("start button", 640, 660, pygame.image.load(resource_urls.start_button).convert())
name_input = UiElement("name input", 640, 585, name_input_img)
lets_go_button = UiElement("lets go button", 625, 575, pygame.image.load(resource_urls.lets_go_button).convert())
buy_button = UiElement("buy button", 860, 680, buy_button_img)
leave_button = UiElement("leave button", 970, 680, leave_button_img)
rest_button = UiElement("rest button", 860, 680, rest_button_img)
mage_learn_button = UiElement("mage learn button", 650, 250, pygame.image.load(resource_urls.learn_button).convert())
fighter_learn_button = UiElement("fighter learn button", 420, 330,
                                 pygame.image.load(resource_urls.learn_button).convert())
scout_learn_button = UiElement("scout learn button", 560, 410, pygame.image.load(resource_urls.learn_button).convert())
barrier_learn_button = UiElement("barrier learn button", 505, 300,
                                 pygame.image.load(resource_urls.skill_learn_button).convert())
hard_strike_learn_button = UiElement("hard strike learn button", 505, 300,
                                     pygame.image.load(resource_urls.skill_learn_button).convert())
sharp_sense_learn_button = UiElement("sharp sense learn button", 505, 300,
                                     pygame.image.load(resource_urls.skill_learn_button).convert())
close_button = UiElement("close button", 975, 135, pygame.image.load(resource_urls.close_button).convert())
quest_button = UiElement("quest button", 860, 680, quest_button_img)
accept_button = UiElement("accept button", 340, 670, accept_button_img)
decline_button = UiElement("decline button", 450, 670, decline_button_img)
hearth_button = UiElement("hearth button", 860, 25, hearth_button_img)
save_button = UiElement("save button", 970, 25, save_button_img)
yes_button = UiElement("yes button", 450, 394, yes_button_img)
no_button = UiElement("no button", 564, 394, no_button_img)
skill_bar = UiElement("skill bar", 855, 615, pygame.image.load(resource_urls.skill_bar).convert())
no_role_attack_button = UiElement("no role attack button", 750, 627, no_role_attack_button_img)
mage_attack_button = UiElement("mage attack button", 750, 627, mage_attack_button_img)
fighter_attack_button = UiElement("fighter attack button", 750, 627, fighter_attack_button_img)
scout_attack_button = UiElement("scout attack button", 750, 627, scout_attack_button_img)
barrier_button = UiElement("barrier button", 820, 627, barrier_button_img)
hard_strike_button = UiElement("hard strike button", 820, 627, strike_button_img)
sharp_sense_button = UiElement("sharp sense button", 820, 627, sense_button_img)
enemy_status = UiElement("enemy status", 855, 680, pygame.image.load(resource_urls.enemy_status).convert())
hp_bar = UiElement("health bar", 165, 25, hp_100)
en_bar = UiElement("energy bar", 165, 45, en_100)
xp_bar = UiElement("xp bar", 165, 65, xp_100)
journal = UiElement("journal", 770, 380, journal_window_img)
level_up_win = UiElement("level up window", 165, 132, pygame.image.load(resource_urls.level_up).convert())
character_sheet = UiElement("character sheet", 770, 380, character_window_img)
mage_book = UiElement("mage book", 670, 375, mage_book_img)
fighter_book = UiElement("fighter book", 670, 375, fighter_book_img)
scout_book = UiElement("scout book", 670, 375, scout_book_img)
quest_logs_1 = Item("quest logs", "quest", 60, 540, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_2 = Item("quest logs", "quest", 315, 560, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_3 = Item("quest logs", "quest", 415, 435, pygame.image.load(resource_urls.quest_logs).convert())
quest_logs_4 = Item("quest logs", "quest", 100, 540, pygame.image.load(resource_urls.quest_logs).convert())
npc_name_plate = UiElement("npc name plate", 640, 192, pygame.image.load(resource_urls.npc_name_plate).convert())
buy_inventory = Inventory("buy inventory", [], 900, 500, pygame.image.load(resource_urls.buy_inventory).convert())
knowledge_window = UiElement("knowledge window", 635, 680, pygame.image.load(resource_urls.knowledge_window).convert())
garan_quest_window = UiElement("garan quest window", 262, 442, garan_quest)
maurelle_quest_window = UiElement("maurelle quest window", 262, 442, maurelle_quest)
guard_quest_window = UiElement("guard quest window", 262, 442, guard_quest)
message_box = UiElement("message box", 173, 650, pygame.image.load(resource_urls.message_box))
status_bar_backdrop = UiElement("bar backdrop", 165, 45, pygame.image.load(resource_urls.bar_backdrop))
enemy_status_bar_backdrop = UiElement("enemy bar backdrop", 700, 90,
                                      pygame.image.load(resource_urls.enemy_bar_backdrop))
quest_star_garan = UiElement("quest star garan", 210, 390, quest_start_star, )
quest_star_maurelle = UiElement("quest star maurelle", 760, 480, quest_start_star)
quest_star_guard = UiElement("quest star guard", 430, 75, quest_start_star)
player_battle_sprite = BattleCharacter("stan battle", 320, 460, player_no_role_amuna_battle)
snake_battle_sprite = BattleCharacter("snake battle", 715, 250, snake_battle)
ghoul_battle_sprite = BattleCharacter("ghoul battle", 700, 250, ghoul_battle)
nascent_gate_popup = UiElement("nascent gate popup", 418, 200,
                               pygame.image.load(resource_urls.nascent_gate_popup_url).convert())

# setting font and size for text to screen updates
font = pygame.font.SysFont('freesansbold.ttf', 22, bold=False, italic=False)
level_up_font = pygame.font.SysFont('freesansbold.ttf', 28, bold=True, italic=False)
name_input_font = pygame.font.SysFont('freesansbold.ttf', 32, bold=True, italic=False)

# groups for sprites
quest_items = pygame.sprite.Group()
npcs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()
buildings = pygame.sprite.Group()
environments = pygame.sprite.Group()
user_interface = pygame.sprite.Group()
enemy_hp_bars = pygame.sprite.Group()
most_sprites = pygame.sprite.Group()
non_sprite_sheets = pygame.sprite.Group()
# specific enemy groups for movement and respawn
snakes = pygame.sprite.Group()
snakes.add(snake_1, snake_2, snake_3, snake_4)
ghouls = pygame.sprite.Group()
ghouls.add(ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
# adding most sprite objects to groups
npcs.add(npc_garan, npc_maurelle, npc_guard)
enemies.add(snake_1, snake_2, snake_3, snake_4, ghoul_low_1, ghoul_low_2, ghoul_low_3, ghoul_low_4)
trees.add(pine_tree_1, pine_tree_2, pine_tree_3)
buildings.add(seldon_inn, seldon_shop, seldon_academia)
user_interface.add(rest_button, buy_button, leave_button, character_button, journal_button, save_button, hearth_button,
                   message_box)
# all environment sprites for collision detection
environments.add(trees, buildings)
# quest item sprites for gathering
quest_items.add(quest_logs_1, quest_logs_2, quest_logs_3, quest_logs_4, rohir_gate)
# adding most sprites to this group for drawing and related functions
most_sprites.add(npcs, trees, buildings, quest_items, enemies, seldon_hearth, rohir_gate)
# group to set transparency to sprites that don't have it set in the spritesheet class constructor
non_sprite_sheets.add(trees, seldon_hearth, quest_items, skill_bar, lets_go_button,
                      mage_learn_button, fighter_learn_button, scout_learn_button,
                      barrier_learn_button, hard_strike_learn_button, sharp_sense_learn_button,
                      character_select_overlay, amuna_select_overlay, nuldar_select_overlay, sorae_select_overlay,
                      start_button, nascent_gate)
for non_sprite_sheet_sprite in non_sprite_sheets:
    non_sprite_sheet_sprite.surf.set_colorkey((255, 255, 255), RLEACCEL)

# code related to sound effects that will be used later
# pygame.mixer.music.load("Electric_1.mp3")
# pygame.mixer.music.play(loops=-1)
# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
# collision_sound = pygame.mixer.Sound("Collision.ogg")
# Set the base volume for all sounds
# move_up_sound.set_volume(0.5)
# move_down_sound.set_volume(0.5)
# collision_sound.set_volume(0.5)

# main loop variables --------------------------------------------------------------------------------------------------
game_running = True
new_game_chosen = False
continue_game_chosen = False
start_chosen = False
# conditions for character selection screen to switch screens
amuna_race_selected = True
nuldar_race_selected = False
sorae_race_selected = False
# condition to check if player has clicked on the name input text box on character creation screen
name_input_selected = False
# main iteration condition checks for player location in game
in_over_world = True
in_battle = False
in_shop = False
in_inn = False
in_academia = False
in_npc_interaction = False
# condition to check if player has chosen to interact with object
interacted = False
# condition to allow or block player movement
movement_able = True
# condition for battle sequences so that buttons can't be spam clicked
combat_cooldown = False
# condition to check if combat occurred on current game loop iteration to update sprites at end of loop
combat_happened = False
# condition to check if buy button is clicked in shop
buy_clicked = False
# condition to check if rest button is clicked in inn
rest_clicked = False
# conditions to check if role books have been clicked in academia
mage_learn_clicked = False
fighter_learn_clicked = False
scout_learn_clicked = False
# condition to check if the character button has been clicked
character_button_clicked = False
# condition to check if the journal button has been clicked
journal_button_clicked = False
# condition to check if hearth button has been clicked to move player and set fade animation
hearth_clicked = False
# condition to check if player has hearthed
hearthed = False
# condition to check if player has started combat encounter with enemy to clear message box (before adding combat text)
encounter_started = False
# condition to check if player has bought an item from shop
item_bought = False
# condition to check if player has rested in an inn
rested = False
# conditions to check if player has a learned these skills from the academia
barrier_learned = False
hard_strike_learned = False
sharp_sense_learned = False
# condition to check if player gear has been checked for stat bonus
gear_checked = False
# condition to check if player weapon has been checked for stat bonus
weapon_checked = False
# conditions to check whether these role skills are active
barrier_active = False
sharp_sense_active = False
# condition that checks if inn screen has been faded when player rests
faded_inn_screen = False
# condition to check if fighter skill hard strike has been used for applying the animation
hard_strike = False
# condition to check if quest button has been clicked in npc interation
quest_clicked = False
# condition to check if knowledge notification has been shown to player
knowledge_academia_show = False
# condition to check if player has clicked on knowledge notification to hide it
knowledge_window_clicked = False
# condition to check if rest notification has been shown to player
rest_recover_show = False
# condition to check if player has clicked on rest notification to hide it
rest_window_clicked = False
# condition to check if gear notification has been shown to player
shop_gear_show = False
# condition to check if player has clicked on gear notification to hide it
shop_window_clicked = False
# condition to check if player has saved game
saved = False
# condition to check if player has pressed enter key during character selection screen
entered = False
# list to contain current player items for display
player_items = []
# list to contain current player equipment for display
player_equipment = []
# list to contain buy inventory window for display within shop
buy_shop_elements = []
# list to contain current shop items for display
shopkeeper_items = []
# list to contain screen size elements for display
display_elements = []
# list to contain skill learn items for the academia instance
skill_learn_items = []
# list to contain books in academia instance for displaying
books = []
# list to contain knowledge notification when player knowledge is 40
knowledge_academia_window = []
# list to contain rest notification when player health is less than 50
rest_recover_window = []
# list to contain gear notification when player gets weapon
shop_gear_window = []
# list to contain save window elements when player saves game (if overwriting previous)
save_check_window = []
# list to contain popup window for no save data found at start
save_data_window = []
# list to contain nascent grove gate interaction popup
nascent_gate_popup_container = []
# combat text strings to be updated on scenario, shown on UI message box
# initially set to these default strings but will be overwritten
info_text_1 = ""
info_text_2 = ""
info_text_3 = ""
info_text_4 = ""
# string to get character name input from user when selecting a character
character_name_input = ''
# text updates from battle instance to apply to main over-world message box
battle_info_to_return_to_main_loop = {"experience": 0, "item dropped": "", "leveled_up": False, "knowledge": ""}

# start time measurements to activate certain functions (enemy/npc movement, message box clearing)
enemy_tic = time.perf_counter()
npc_tic = time.perf_counter()
info_tic = time.perf_counter()
loot_tic = time.perf_counter()
walk_tic = time.perf_counter()

# main loop ------------------------------------------------------------------------------------------------------------
while game_running:

    # update player position each iteration
    player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

    if not new_game_chosen and not continue_game_chosen and not start_chosen:
        screen.blit(start_screen, (0, 0))
        screen.blit(new_game_button.surf, new_game_button.rect)
        screen.blit(continue_button.surf, continue_button.rect)
        for element in save_data_window:
            screen.blit(element.surf, element.rect)
        # user input events such as key presses or UI interaction
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # player chooses to start a new game or continue from previous
                if new_game_button.rect.collidepoint(pos):
                    new_game_chosen = True
                if continue_button.rect.collidepoint(pos):
                    continue_game_chosen = True
                if save_absent.rect.collidepoint(pos):
                    save_data_window.clear()
            elif event.type == QUIT:
                exit()
        pygame.display.flip()

    # character selection for new game ---------------------------------------------------------------------------------
    if new_game_chosen:
        # amuna race selected on character selection screen
        if amuna_race_selected:
            screen.blit(amuna_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(amuna_select_overlay.surf, amuna_select_overlay.rect)
            screen.blit(amuna_character.surf, amuna_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    # if enter key is pressed, de-select name box and proceed
                    if event.key == K_RETURN:
                        name_input_selected = False
                        entered = True
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # player clicks on the box to type name
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_empty_img)
                            name_input_selected = True
                # player amuna race selection, set conditions to go to amuna select screen
                if amuna_button.rect.collidepoint(pos):
                    amuna_race_selected = True
                    nuldar_race_selected = False
                    sorae_race_selected = False
                # player amuna race selection, set conditions to go to amuna select screen
                if nuldar_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = True
                    sorae_race_selected = False
                # player amuna race selection, set conditions to go to amuna select screen
                if sorae_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = False
                    sorae_race_selected = True
                # get whatever the player typed in name box and chosen race and start game
                if start_button.rect.collidepoint(pos) or entered:
                    if len(character_name_input) > 0:
                        player.name = str(character_name_input)
                    else:
                        player.name = "default"
                    player.race = "amuna"
                    player.surf = player_no_role_amuna_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True
                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

        # sorae race selected on character selection screen
        if sorae_race_selected:
            screen.blit(sorae_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(sorae_select_overlay.surf, sorae_select_overlay.rect)
            screen.blit(sorae_character.surf, sorae_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_RETURN:
                        name_input_selected = False
                        entered = True
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_empty_img)
                            name_input_selected = True
                if amuna_button.rect.collidepoint(pos):
                    amuna_race_selected = True
                    nuldar_race_selected = False
                    sorae_race_selected = False
                if nuldar_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = True
                    sorae_race_selected = False
                if sorae_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = False
                    sorae_race_selected = True
                if start_button.rect.collidepoint(pos) or entered:
                    if len(character_name_input) > 0:
                        player.name = str(character_name_input)
                    else:
                        player.name = "default"
                    player.race = "sorae"
                    player.surf = player_no_role_sorae_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True
                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

        # nuldar race selected on character selection screen
        if nuldar_race_selected:
            screen.blit(nuldar_character_screen, (0, 0))
            screen.blit(character_select_overlay.surf, character_select_overlay.rect)
            screen.blit(amuna_button.surf, amuna_button.rect)
            screen.blit(nuldar_button.surf, nuldar_button.rect)
            screen.blit(sorae_button.surf, sorae_button.rect)
            screen.blit(nuldar_select_overlay.surf, nuldar_select_overlay.rect)
            screen.blit(nuldar_character.surf, nuldar_character.rect)
            screen.blit(start_button.surf, start_button.rect)
            screen.blit(name_input.surf, name_input.rect)
            character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
            screen.blit(character_name_surface, (605, 575))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_RETURN:
                        name_input_selected = False
                        entered = True
                    if event.key == K_BACKSPACE:
                        if name_input_selected:
                            character_name_input = character_name_input[:-1]
                    else:
                        if name_input_selected:
                            if len(character_name_input) < 12:
                                character_name_input += event.unicode
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if name_input.rect.collidepoint(pos):
                        if name_input_selected:
                            if len(character_name_input) < 1:
                                name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_img)
                            name_input_selected = False
                        else:
                            name_input.update(name_input.x_coordinate, name_input.y_coordinate, name_input_empty_img)
                            name_input_selected = True
                if amuna_button.rect.collidepoint(pos):
                    amuna_race_selected = True
                    nuldar_race_selected = False
                    sorae_race_selected = False
                if nuldar_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = True
                    sorae_race_selected = False
                if sorae_button.rect.collidepoint(pos):
                    amuna_race_selected = False
                    nuldar_race_selected = False
                    sorae_race_selected = True
                if start_button.rect.collidepoint(pos) or entered:
                    if len(character_name_input) > 0:
                        player.name = str(character_name_input)
                    else:
                        player.name = "default"
                    player.race = "nuldar"
                    player.surf = player_no_role_nuldar_down_1
                    player.current_zone = "nascent"
                    in_over_world = True
                    new_game_chosen = False
                    start_chosen = True
                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

    # continue game selected on start screen. try to load player info from save_game file
    if continue_game_chosen:
        try:
            with open("save_game", "rb") as f:
                player_load_info = pickle.load(f)
                player.name = player_load_info["name"]
                player.level = player_load_info["level"]
                player.health = player_load_info["hp"]
                player.energy = player_load_info["en"]
                player.offense = player_load_info["offense"]
                player.defence = player_load_info["defense"]
                player.experience = player_load_info["xp"]
                player.race = player_load_info["race"]
                player.role = player_load_info["role"]
                if player.race == "amuna":
                    if player.role == "mage":
                        player.surf = player_mage_amuna_down_1
                    if player.role == "fighter":
                        player.surf = player_fighter_amuna_down_1
                    if player.role == "scout":
                        player.surf = player_scout_amuna_down_1
                    else:
                        player.surf = player_no_role_amuna_down_1
                if player.race == "nuldar":
                    if player.role == "mage":
                        player.surf = player_mage_nuldar_down_1
                    if player.role == "fighter":
                        player.surf = player_fighter_nuldar_down_1
                    if player.role == "scout":
                        player.surf = player_scout_nuldar_down_1
                    else:
                        player.surf = player_no_role_nuldar_down_1
                if player.race == "sorae":
                    if player.role == "mage":
                        player.surf = player_mage_sorae_down_1
                    if player.role == "fighter":
                        player.surf = player_fighter_sorae_down_1
                    if player.role == "scout":
                        player.surf = player_scout_sorae_down_1
                    else:
                        player.surf = player_no_role_sorae_down_1
                # clear default starting items and load personal player items from save file
                # create new item sprite based on name from file
                player.items.clear()
                for item in player_load_info["inventory"]:
                    if item == "health potion":
                        player.items.append(Item("health potion", "potion", 200, 200, health_pot_img))
                    if item == "energy potion":
                        player.items.append(Item("energy potion", "potion", 200, 200, energy_pot_img))
                    if item == "basic staff":
                        player.items.append(Item("basic staff", "mage", 200, 200, basic_staff_img))
                    if item == "basic sword":
                        player.items.append(Item("basic sword", "fighter", 200, 200, basic_sword_img))
                    if item == "basic bow":
                        player.items.append(Item("basic bow", "scout", 200, 200, basic_bow_img))
                    if item == "basic robes":
                        player.items.append(Item("basic robes", "mage", 200, 200, basic_robes_img))
                    if item == "basic armor":
                        player.items.append(Item("basic armor", "fighter", 200, 200, basic_armor_img))
                    if item == "basic tunic":
                        player.items.append(Item("basic tunic", "scout", 200, 200, basic_tunic_img))
                    if item == "shiny rock":
                        player.items.append(Item("shiny rock", "rock", 200, 200, shiny_rock_img))
                    if item == "bone dust":
                        player.items.append(Item("bone dust", "dust", 200, 200, bone_dust_img))
                for equipped_item in player_load_info["equipment"]:
                    if equipped_item == "basic staff":
                        player.equipment["weapon"] = Item("basic staff", "mage", 200, 200, basic_staff_img)
                    if equipped_item == "basic sword":
                        player.equipment["weapon"] = Item("basic sword", "fighter", 200, 200, basic_sword_img)
                    if equipped_item == "basic bow":
                        player.equipment["weapon"] = Item("basic bow", "scout", 200, 200, basic_bow_img)
                    if equipped_item == "basic robes":
                        player.equipment["chest"] = Item("basic robes", "mage", 200, 200, basic_robes_img)
                    if equipped_item == "basic armor":
                        player.equipment["chest"] = Item("basic armor", "fighter", 200, 200, basic_armor_img)
                    if equipped_item == "basic tunic":
                        player.equipment["chest"] = Item("basic tunic", "scout", 200, 200, basic_tunic_img)
                player.current_quests = player_load_info["quests"]
                player.quest_progress = player_load_info["quest progress"]
                player.quest_status = player_load_info["quest status"]
                player.quest_complete = player_load_info["quest complete"]
                player.knowledge = player_load_info["knowledge"]
                player.skills_mage = player_load_info["mage skills"]
                player.skills_fighter = player_load_info["fighter skills"]
                player.skills_scout = player_load_info["scout skills"]
                barrier_learned = player_load_info["learned"]["barrier"]
                hard_strike_learned = player_load_info["learned"]["strike"]
                sharp_sense_learned = player_load_info["learned"]["sense"]
                player.rupees = player_load_info["rupees"]
                player.reputation = player_load_info["reputation"]
                player.current_zone = player_load_info["zone"]
                if player.current_zone == "nascent":
                    player.x_coordinate = 760
                    player.y_coordinate = 510
                    player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                if player.current_zone == "seldon":
                    player.x_coordinate = 425
                    player.y_coordinate = 690
                    player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                if player.current_zone == "korlok":
                    player.x_coordinate = 500
                    player.y_coordinate = 500
                    player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                saved = player_load_info["saved"]
                start_chosen = True
                continue_game_chosen = False
        # no save file found, show a notification to player and reset condition
        except FileNotFoundError:
            continue_game_chosen = False
            save_data_window.append(save_absent)
            pass

    # if player has chosen to start game -------------------------------------------------------------------------------
    if start_chosen:
        # start game clock and set fonts
        clock = pygame.time.Clock()
        # if player is currently alive
        if player.alive_status:

            # if player is in nascent grove (starting area) ------------------------------------------------------------
            if player.current_zone == "nascent" and in_over_world:
                screen.blit(nascent_grove_bg, (0, 0))
                screen.blit(nascent_gate.surf, nascent_gate.rect)
                screen.blit(player.surf, player.rect)
                for popup in nascent_gate_popup_container:
                    screen.blit(popup.surf, popup.rect)

                walking_return_nascent = walk_time(walk_tic)
                if walking_return_nascent["reset"]:
                    walk_tic = time.perf_counter()
                if movement_able:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                        player.update("right", "nascent", walking_return_nascent["total time"])
                    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                        player.update("left", "nascent", walking_return_nascent["total time"])
                    if pressed_keys[K_w] or pressed_keys[K_UP]:
                        player.update("up", "nascent", walking_return_nascent["total time"])
                    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                        player.update("down", "nascent", walking_return_nascent["total time"])

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                        if event.key == K_f:
                            if pygame.sprite.collide_rect(player, nascent_gate):
                                interacted = True
                    elif event.type == QUIT:
                        exit()

                if pygame.sprite.collide_rect(player, nascent_gate):
                    nascent_gate_popup_container.append(nascent_gate_popup)
                    if interacted:
                        nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate, nascent_gate_open)
                        if player.y_coordinate > 300:
                            player.y_coordinate = 215
                        else:
                            player.y_coordinate = 375
                        interacted = False
                else:
                    nascent_gate_popup_container.clear()
                    nascent_gate.update(nascent_gate.x_coordinate, nascent_gate.y_coordinate, nascent_gate_closed)

                # move player to seldon district when they approach nascent grove exit
                if player.x_coordinate > 700 and player.y_coordinate < 80:
                    player.current_zone = "seldon"
                    in_over_world = True
                    player.x_coordinate = 425
                    player.y_coordinate = 690

            # ----------------------------------------------------------------------------------------------------------
            # if player is in stardust outpost -------------------------------------------------------------------------
            if player.current_zone == "stardust" and in_over_world:
                screen.blit(stardust_outpost_bg, (0, 0))

                # hearth button is clicked, sets fade transition for hearth screen and then back to district bg --------
                if hearth_clicked:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 200):
                        seldon_hearth_screen.set_alpha(alpha)
                        screen.blit(seldon_hearth_screen, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    hearth_clicked = False
                    hearthed = True
                if hearthed:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 50):
                        seldon_district_bg.set_alpha(alpha)
                        screen.blit(seldon_district_bg, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    seldon_district_bg.set_alpha(255)
                    screen.blit(seldon_district_bg, (0, 0))
                    pygame.display.flip()
                    hearthed = False
                    info_text_1 = "You recalled to the hearth stone."
                # ------------------------------------------------------------------------------------------------------

                player_info_and_ui_updates()

                walking_return_stardust = walk_time(walk_tic)
                if walking_return_stardust["reset"]:
                    walk_tic = time.perf_counter()
                if movement_able:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                        player.update("right", "stardust", walking_return_stardust["total time"])
                    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                        player.update("left", "stardust", walking_return_stardust["total time"])
                    if pressed_keys[K_w] or pressed_keys[K_UP]:
                        player.update("up", "stardust", walking_return_stardust["total time"])
                    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                        player.update("down", "stardust", walking_return_stardust["total time"])

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                        if event.key == K_f:
                            if pygame.sprite.spritecollideany(player, most_sprites):
                                interacted = True
                    elif event.type == QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if hearth_button.rect.collidepoint(pos):
                            hearth_clicked = True
                            player.current_zone = "seldon"
                            player.x_coordinate = 850
                            player.y_coordinate = 650
                        if save_button.rect.collidepoint(pos):
                            try:
                                with open("save_game", "rb") as f:
                                    saved = True
                            except FileNotFoundError:
                                saved = False
                                pass
                            if saved:
                                save_check_window.append(save_check)
                                save_check_window.append(yes_button)
                                save_check_window.append(no_button)
                            if not saved:
                                save_game()
                                saved = True
                                info_text_1 = "You saved your game. "
                        if yes_button.rect.collidepoint(pos):
                            save_game()
                            save_check_window.clear()
                            info_text_1 = "You saved your game. "
                        if no_button.rect.collidepoint(pos):
                            save_check_window.clear()

                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                            else:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                character_button_clicked = True
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                            else:
                                drawing_functions.journal_info_draw(journal, player, font, True)
                                journal_button_clicked = True

                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # move player to seldon district when they approach nascent grove exit
                if player.x_coordinate > 925 and 175 < player.y_coordinate < 275:
                    player.current_zone = "seldon"
                    in_over_world = True
                    player.x_coordinate = 125
                    player.y_coordinate = 375

            # ----------------------------------------------------------------------------------------------------------
            # if player is in seldon district over world ---------------------------------------------------------------
            if player.current_zone == "seldon" and in_over_world:
                screen.blit(seldon_district_bg, (0, 0))

                # hearth button is clicked, sets fade transition for hearth screen and then back to district bg --------
                if hearth_clicked:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 200):
                        seldon_hearth_screen.set_alpha(alpha)
                        screen.blit(seldon_hearth_screen, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    hearth_clicked = False
                    hearthed = True
                if hearthed:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 50):
                        seldon_district_bg.set_alpha(alpha)
                        screen.blit(seldon_district_bg, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    seldon_district_bg.set_alpha(255)
                    screen.blit(seldon_district_bg, (0, 0))
                    pygame.display.flip()
                    hearthed = False
                    info_text_1 = "You recalled to the hearth stone."
                # ------------------------------------------------------------------------------------------------------
                # switches between 1 and 0 to select a left or right direction for enemy sprite to move
                enemy_switch = 1
                # gets defeated enemy count and will respawn a new enemy type if count is greater than specified
                enemy_respawn()

                # try to blit elements if they exist in group or list
                try:
                    for entity in most_sprites:
                        screen.blit(entity.surf, entity.rect)
                    for enemy_sprite in enemies:
                        screen.blit(enemy_sprite.surf, enemy_sprite.rect)
                except TypeError:
                    pass

                # quest stars for npcs that update based on player quest progress
                # ------------------------------------------------------------------------------------------------------
                if not player.quest_complete["sneaky snakes"]:
                    screen.blit(quest_star_garan.surf, quest_star_garan.rect)
                if player.quest_progress["sneaky snakes"] == 4:
                    quest_star_garan.update(210, 390, quest_complete_star)
                if player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
                    quest_star_garan.update(210, 390, quest_progress_star)
                if not player.quest_complete["village repairs"]:
                    screen.blit(quest_star_maurelle.surf, quest_star_maurelle.rect)
                if player.quest_progress["village repairs"] == 4:
                    quest_star_maurelle.update(760, 480, quest_complete_star)
                if player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
                    quest_star_maurelle.update(760, 480, quest_progress_star)
                if not player.quest_complete["ghouled again"]:
                    screen.blit(quest_star_guard.surf, quest_star_guard.rect)
                if player.quest_progress["ghouled again"] == 4:
                    quest_star_guard.update(430, 75, quest_complete_star)
                if player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
                    quest_star_guard.update(430, 75, quest_progress_star)
                # ------------------------------------------------------------------------------------------------------

                player_info_and_ui_updates()

                # pop up notifications for situations like low health or first weapon acquire
                if not knowledge_academia_show:
                    if player.knowledge["mage"] == 50 or player.knowledge["fighter"] == 50 or \
                            player.knowledge["scout"] == 50:
                        knowledge_academia_window.append(knowledge_academia)
                        knowledge_academia_show = True
                if knowledge_academia_show:
                    if knowledge_window_clicked:
                        knowledge_academia_window.clear()
                if not rest_recover_show:
                    if player.health < 50:
                        rest_recover_window.append(rest_recover)
                        rest_recover_show = True
                if rest_recover_show:
                    if rest_window_clicked:
                        rest_recover_window.clear()

                # draw pop up notifications on top of everything else
                for knowledge_window_notification in knowledge_academia_window:
                    screen.blit(knowledge_window_notification.surf, knowledge_window_notification.rect)
                for rest_window in rest_recover_window:
                    screen.blit(rest_window.surf, rest_window.rect)

                # if battle happened, get battle info (item or experience gained) and apply to message box
                if battle_info_to_return_to_main_loop["item dropped"] != "":
                    info_text_3 = str(battle_info_to_return_to_main_loop["item dropped"])
                    info_text_4 = str(battle_info_to_return_to_main_loop["experience"]) + "and " + \
                                  str(battle_info_to_return_to_main_loop["knowledge"])
                if battle_info_to_return_to_main_loop["leveled_up"]:
                    drawing_functions.level_up_draw(level_up_win, player, font, True)

                # ------------------------------------------------------------------------------------------------------
                # all in-game events such as key presses or UI interaction
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        # escape key was pressed, exit game
                        if event.key == K_ESCAPE:
                            exit()
                        # "F" key for player interaction
                        if event.key == K_f:
                            if pygame.sprite.spritecollideany(player, most_sprites):
                                interacted = True
                    elif event.type == QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        # hearth button was clicked, set true for animation and move player to stone
                        if hearth_button.rect.collidepoint(pos):
                            hearth_clicked = True
                            player.x_coordinate = 850
                            player.y_coordinate = 650
                        # save button was clicked. Save player info in dictionary to be loaded later -------------------
                        if save_button.rect.collidepoint(pos):
                            # see if there already exists a save file by trying to read it
                            # if it was opened, set saved condition to true for the save check
                            # if it doesn't find a save file, set saved condition to false for save check
                            try:
                                with open("save_game", "rb") as f:
                                    saved = True
                            except FileNotFoundError:
                                saved = False
                                pass
                            if saved:
                                save_check_window.append(save_check)
                                save_check_window.append(yes_button)
                                save_check_window.append(no_button)
                            if not saved:
                                save_game()
                                saved = True
                                info_text_1 = "You saved your game. "
                        # yes button was clicked to overwrite previous save file
                        if yes_button.rect.collidepoint(pos):
                            save_game()
                            save_check_window.clear()
                            info_text_1 = "You saved your game. "
                        if no_button.rect.collidepoint(pos):
                            save_check_window.clear()
                        # ----------------------------------------------------------------------------------------------
                        # if character button is clicked, call draw function and show elements. second click hides
                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                            else:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                character_button_clicked = True
                        # if journal button is clicked, call draw function and show elements. second click hides
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                            else:
                                drawing_functions.journal_info_draw(journal, player, font, True)
                                journal_button_clicked = True
                        # when player levels up, this lets them click to dismiss the window pop-up
                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)
                        if knowledge_academia.rect.collidepoint(pos) and knowledge_academia_show:
                            knowledge_window_clicked = True
                        if rest_recover.rect.collidepoint(pos) and rest_recover_show:
                            rest_window_clicked = True
                        if shop_gear.rect.collidepoint(pos) and shop_gear_show:
                            shop_window_clicked = True

                    # move player to nascent grove when they approach
                    if 375 < player.x_coordinate < 475 and player.y_coordinate > 700:
                        player.current_zone = "nascent"
                        in_over_world = True
                        player.x_coordinate = 750
                        player.y_coordinate = 125
                    # move player to stardust outpost when they approach
                    if player.x_coordinate < 25 and 325 < player.y_coordinate < 400:
                        player.current_zone = "stardust"
                        in_over_world = True
                        player.x_coordinate = 925
                        player.y_coordinate = 275

                    # player encounters a quest item. check progress and add to if interacted with
                    quest_item = pygame.sprite.spritecollideany(player, quest_items)
                    try:
                        if quest_item.name == "quest logs":
                            if player.quest_status["village repairs"]:
                                info_text_1 = f"Press 'F' key to gather the pine logs."
                                if interacted:
                                    if player.quest_progress["village repairs"] < 4:
                                        player.quest_progress["village repairs"] += 1
                                        info_text_1 = f"You gathered 1 pine log."
                                        quest_item.kill()
                                        interacted = False
                                    else:
                                        info_text_1 = f"You've already gathered these.'."
                                        interacted = False
                        if quest_item.name == "rohir gate":
                            if player.quest_complete["ghouled again"]:
                                info_text_1 = f"Press 'F' key to enter Korlok District."
                                if interacted:
                                    player.current_zone = "korlok"
                                    interacted = False
                            if not player.quest_complete["ghouled again"]:
                                info_text_1 = f"The gate seems to be locked shut."
                                info_text_2 = f"Perhaps the nearby Guard knows why?"
                    except AttributeError:
                        pass

                    # --------------------------------------------------------------------------------------------------
                    # if player collides with enemy sprite, doesn't have combat cooldown,
                    # and chooses to interact with it then get event from button press and start combat encounter
                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        # lets player know if they are in range of enemy they can press f to attack it
                        info_text_1 = f"Press 'F' key to attack {enemy.name}."
                        info_text_2 = f"{enemy.name} level: {enemy.level}"
                        if interacted:
                            if player.race == "amuna":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_amuna_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_amuna_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_amuna_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_amuna_battle)
                            if player.race == "sorae":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_sorae_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_sorae_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_sorae_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_sorae_battle)
                            if player.race == "nuldar":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_nuldar_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_nuldar_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_nuldar_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_nuldar_battle)
                            in_over_world = False
                            in_battle = True

                    # --------------------------------------------------------------------------------------------------
                    # player collides with building, enters if chosen to interact and starts related scenario
                    building = pygame.sprite.spritecollideany(player, buildings)
                    if building:
                        # lets player know if they are in range of building they can press f to enter it
                        info_text_1 = f"Press 'F' key to enter {building.name}."
                        info_text_2 = ""
                        if interacted:
                            in_over_world = False
                            if building.name == "shop":
                                in_shop = True
                            if building.name == "inn":
                                in_inn = True
                            if building.name == "academia":
                                in_academia = True

                    # --------------------------------------------------------------------------------------------------
                    # if player collides with npc sprite and chooses to interact with it
                    npc = pygame.sprite.spritecollideany(player, npcs)
                    if npc:
                        info_text_1 = f"Press 'F' key to talk to {npc.name}."
                        if interacted:
                            if player.race == "amuna":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_amuna_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_amuna_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_amuna_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_amuna_battle)
                            if player.race == "sorae":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_sorae_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_sorae_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_sorae_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_sorae_battle)
                            if player.race == "nuldar":
                                if player.role == "mage":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_mage_nuldar_battle)
                                if player.role == "fighter":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_fighter_nuldar_battle)
                                if player.role == "scout":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_scout_nuldar_battle)
                                if player.role == "":
                                    player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                player_battle_sprite.y_coordinate,
                                                                player_no_role_nuldar_battle)
                            in_over_world = False
                            in_npc_interaction = True

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event, player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event, player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # outside of main event loop ---------------------------------------------------------------------------
                walking_return_seldon = walk_time(walk_tic)
                if walking_return_seldon["reset"]:
                    walk_tic = time.perf_counter()
                if movement_able:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                        player.update("right", "seldon", walking_return_seldon["total time"])
                    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                        player.update("left", "seldon", walking_return_seldon["total time"])
                    if pressed_keys[K_w] or pressed_keys[K_UP]:
                        player.update("up", "seldon", walking_return_seldon["total time"])
                    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                        player.update("down", "seldon", walking_return_seldon["total time"])

                # enemy movement updates -------------------------------------------------------------------------------
                # choose random directions and random enemy to move that direction -------------------------------------
                direction_horizontal = random.choice(["left", "right"])
                direction_vertical = random.choice(["up", "down"])
                move_this_snake = random.choice(snakes.sprites())
                move_this_ghoul = random.choice(ghouls.sprites())
                if movement_able:
                    enemy_toc = time.perf_counter()
                    if enemy_toc - enemy_tic > 1:
                        enemy_tic = time.perf_counter()
                        move_this_snake.update_position([100, 300], [200, 300],
                                                        direction_horizontal, direction_vertical)
                        move_this_ghoul.update_position([700, 900], [200, 300],
                                                        direction_horizontal, direction_vertical)

                # npc movement updates ---------------------------------------------------------------------------------
                # choose random facing direction and random npc to move face that direction ----------------------------
                face_direction = random.choice(["front", "back", "left", "right"])
                face_this_npc = random.choice(npcs.sprites())
                if movement_able:
                    npc_toc = time.perf_counter()
                    if npc_toc - npc_tic > 2:
                        npc_tic = time.perf_counter()
                        if face_direction == "front":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_down)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_down)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_down)
                        if face_direction == "back":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_up)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_up)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_up)
                        if face_direction == "left":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_left)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_left)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_left)
                        if face_direction == "right":
                            if face_this_npc.name == "garan":
                                npc_garan.update(garan_right)
                            if face_this_npc.name == "maurelle":
                                npc_maurelle.update(maurelle_right)
                            if face_this_npc.name == "guard":
                                npc_guard.update(guard_right)

            # ----------------------------------------------------------------------------------------------------------
            # if player is in battle -----------------------------------------------------------------------------------
            if in_battle:
                player_info_and_ui_updates()

                # battle scenario event loop
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                    enemy = pygame.sprite.spritecollideany(player, enemies)
                    if enemy:
                        # update enemy health bar on each iteration
                        enemy.health_bar.update(enemy.health_bar.x_coordinate, enemy.health_bar.y_coordinate,
                                                health_bar_update(enemy))
                        # don't let player attack again immediately by spam clicking button
                        if not combat_cooldown:
                            # if interact key 'f' has been pressed
                            if interacted:
                                # don't allow player to move while in combat
                                movement_able = False
                                # if player has just started combat, clear message box, change condition to True
                                if not encounter_started:
                                    info_text_1 = ""
                                    info_text_2 = ""
                                    info_text_3 = ""
                                    info_text_4 = ""
                                    encounter_started = True
                                # get which button player pressed during combat scenario (attack, skill or run)
                                combat_button = click_handlers.combat_event_button(event, no_role_attack_button,
                                                                                   mage_attack_button,
                                                                                   fighter_attack_button,
                                                                                   scout_attack_button,
                                                                                   barrier_button,
                                                                                   hard_strike_button,
                                                                                   sharp_sense_button)

                                if combat_button == "attack":
                                    # update player character sprite for combat animation
                                    if player.race == "amuna":
                                        if player.role == "mage":
                                            if barrier_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_barrier_amuna_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_amuna_attack)
                                        if player.role == "fighter":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_fighter_amuna_attack)
                                        if player.role == "scout":
                                            if sharp_sense_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_sense_amuna_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_amuna_attack)
                                        if player.role == "":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_no_role_amuna_attack)
                                    if player.race == "sorae":
                                        if player.role == "mage":
                                            if barrier_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_barrier_sorae_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_sorae_attack)
                                        if player.role == "fighter":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_fighter_sorae_attack)
                                        if player.role == "scout":
                                            if sharp_sense_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_sense_sorae_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_sorae_attack)
                                        if player.role == "":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_no_role_sorae_attack)
                                    if player.race == "nuldar":
                                        if player.role == "mage":
                                            if barrier_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_barrier_nuldar_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_mage_nuldar_attack)
                                        if player.role == "fighter":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_fighter_nuldar_attack)
                                        if player.role == "scout":
                                            if sharp_sense_active:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_sense_nuldar_attack)
                                            else:
                                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                            player_battle_sprite.y_coordinate,
                                                                            player_scout_nuldar_attack)
                                        if player.role == "":
                                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                        player_battle_sprite.y_coordinate,
                                                                        player_no_role_nuldar_attack)

                                    # update to attacking sprite surface for combat animation --------------------------
                                    if enemy.kind == "snake":
                                        snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                   snake_battle_sprite.y_coordinate,
                                                                   snake_attack)
                                    if enemy.kind == "ghoul":
                                        ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                   ghoul_battle_sprite.y_coordinate,
                                                                   ghoul_attack)

                                    # ----------------------------------------------------------------------------------
                                    # combat event function that handles and returns damage and health
                                    combat_events = attack_scenario(enemy, "attack")
                                    combat_happened = True
                                    # add all combat scenario happenings from function to message box
                                    # if any of the values are currently zero, or no, return blank string
                                    if combat_events["damage done"] == 0:
                                        info_text_1 = ""
                                    else:
                                        info_text_1 = str(combat_events["damage done"])
                                    if combat_events["damage taken"] == 0:
                                        info_text_2 = ""
                                    else:
                                        info_text_2 = str(combat_events["damage taken"])

                                    # adds item dropped and experienced gained messages to box if enemy was defeated
                                    # appends to dictionary to return to main loop outside of battle
                                    if combat_events["enemy defeated"]:
                                        if combat_events["item dropped"] != "No":
                                            battle_info_to_return_to_main_loop["item dropped"] = \
                                                str(combat_events["item dropped"])
                                        if combat_events["experience gained"] != 0:
                                            battle_info_to_return_to_main_loop["experience"] = \
                                                str(combat_events["experience gained"])
                                    # if enemy was defeated and player leveled up, add messages related to box
                                    if combat_events["enemy defeated"]:
                                        if combat_events["level up status"] != "":
                                            battle_info_to_return_to_main_loop["leveled_up"] = True

                                    # if player was successful in defeating enemy, combat ends, movement is allowed
                                    # set combat happened false, allowing iterations to continue without cooldown
                                    # reset encounter_started condition so that next enemy will clear message box
                                    if combat_events["enemy defeated"]:
                                        # player will gain knowledge based on their current role
                                        if player.role == "mage":
                                            player.knowledge["mage"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 mage knowledge gained."
                                        if player.role == "fighter":
                                            player.knowledge["fighter"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 fighter knowledge gained."
                                        if player.role == "scout":
                                            player.knowledge["scout"] += 10
                                            battle_info_to_return_to_main_loop["knowledge"] = \
                                                "10 scout knowledge gained."
                                        # if barrier is active on enemy defeat, restore original defence and set off
                                        if barrier_active:
                                            barrier_active = False
                                            player.defence = original_defence
                                        # if sharp sense is active on enemy defeat, restore original offense
                                        if sharp_sense_active:
                                            sharp_sense_active = False
                                            player.offense = original_offense

                                        movement_able = True
                                        combat_happened = False
                                        interacted = False
                                        encounter_started = False
                                        in_battle = False
                                        in_over_world = True

                                # skill in skill bar slot was clicked
                                # (buffs) mage -> barrier [defence], scout -> sharp sense [offense]
                                if combat_button == "skill 1":
                                    # make sure player has enough energy to use the skill
                                    if player.energy > 34:
                                        # player is a mage and uses the barrier spell. Set barrier active to true
                                        # giving them 20 additional defence and subtract 35 energy
                                        # save original defence value to be re applied upon enemy or player defeat
                                        if player.role == "mage":
                                            if barrier_learned:
                                                if not barrier_active:
                                                    info_text_1 = "Barrier spell is active."
                                                    info_text_2 = "You have gained 10 defence."
                                                    barrier_active = True
                                                    original_defence = player.defence
                                                    player.defence += 10
                                                    player.energy -= 35
                                                else:
                                                    info_text_1 = "Barrier spell is already active."
                                        # player is a scout and uses sharp sense. Set sharp sense active to true
                                        # giving them 20 additional offense and subtract 35 energy
                                        # save original offense value to be re applied upon enemy or player defeat
                                        if player.role == "scout":
                                            if sharp_sense_learned:
                                                if not sharp_sense_active:
                                                    info_text_1 = "Sharp sense is active."
                                                    info_text_2 = "You have gained 20 offense."
                                                    sharp_sense_active = True
                                                    original_offense = player.offense
                                                    player.offense += 20
                                                    player.energy -= 35
                                                else:
                                                    info_text_1 = "Sharp sense is already active."

                                        # player is a fighter and uses hard strike. This uses the standard "attack"
                                        # scenario from above, with the input being changed to the skill instead of
                                        # attack to trigger a different damage value within the attack function
                                        if player.role == "fighter":
                                            if hard_strike_learned:
                                                hard_strike = True
                                                # update animations for hard strike attack -----------------------------
                                                if player.race == "amuna":
                                                    if player.role == "fighter":
                                                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                                    player_battle_sprite.y_coordinate,
                                                                                    player_fighter_amuna_strike)
                                                if player.race == "sorae":
                                                    if player.role == "fighter":
                                                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                                    player_battle_sprite.y_coordinate,
                                                                                    player_fighter_sorae_strike)
                                                if player.race == "nuldar":
                                                    if player.role == "fighter":
                                                        player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                                                    player_battle_sprite.y_coordinate,
                                                                                    player_fighter_nuldar_strike)
                                                if enemy.kind == "snake":
                                                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                                                               snake_battle_sprite.y_coordinate,
                                                                               snake_attack)
                                                if enemy.kind == "ghoul":
                                                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                                                               ghoul_battle_sprite.y_coordinate,
                                                                               ghoul_attack)
                                                # ----------------------------------------------------------------------

                                                combat_events = attack_scenario(enemy, "skill 1")
                                                combat_happened = True
                                                player.energy -= 35
                                                if combat_events["damage done"] == 0:
                                                    info_text_1 = ""
                                                else:
                                                    info_text_1 = str(combat_events["damage done"])
                                                if combat_events["damage taken"] == 0:
                                                    info_text_2 = ""
                                                else:
                                                    info_text_2 = str(combat_events["damage taken"])
                                                if combat_events["enemy defeated"]:
                                                    if combat_events["item dropped"] != "No":
                                                        battle_info_to_return_to_main_loop["item dropped"] = \
                                                            str(combat_events["item dropped"])
                                                    if combat_events["experience gained"] != 0:
                                                        battle_info_to_return_to_main_loop["experience"] = \
                                                            str(combat_events["experience gained"])
                                                if combat_events["enemy defeated"]:
                                                    if combat_events["level up status"] != "":
                                                        battle_info_to_return_to_main_loop["leveled_up"] = True
                                                if combat_events["enemy defeated"]:
                                                    if player.role == "fighter":
                                                        player.knowledge["fighter"] += 10
                                                        battle_info_to_return_to_main_loop["knowledge"] = \
                                                            "10 fighter knowledge gained."

                                                    movement_able = True
                                                    combat_happened = False
                                                    interacted = False
                                                    encounter_started = False
                                                    in_battle = False
                                                    in_over_world = True
                                    else:
                                        info_text_1 = "Not enough energy to use this skill."

                # outside of battle event loop -------------------------------------------------------------------------
                # battle scene and enemy are drawn to screen -----------------------------------------------------------
                try:
                    if player.current_zone == "seldon":
                        screen.blit(seldon_district_battle, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(skill_bar.surf, skill_bar.rect)
                        if player.role == "mage":
                            screen.blit(mage_attack_button.surf, mage_attack_button.rect)
                            if player.skills_mage["skill 2"] == "barrier":
                                screen.blit(barrier_button.surf, barrier_button.rect)
                        if player.role == "fighter":
                            screen.blit(fighter_attack_button.surf, fighter_attack_button.rect)
                            if player.skills_fighter["skill 2"] == "hard strike":
                                screen.blit(hard_strike_button.surf, hard_strike_button.rect)
                        if player.role == "scout":
                            screen.blit(scout_attack_button.surf, scout_attack_button.rect)
                            if player.skills_scout["skill 2"] == "sharp sense":
                                screen.blit(sharp_sense_button.surf, sharp_sense_button.rect)
                        if player.role == "":
                            screen.blit(no_role_attack_button.surf, no_role_attack_button.rect)
                        if enemy.name == "snake":
                            screen.blit(snake_battle_sprite.surf, snake_battle_sprite.rect)
                        if enemy.name == "ghoul":
                            screen.blit(ghoul_battle_sprite.surf, ghoul_battle_sprite.rect)

                        # draw player after enemy to show animations on top of enemy and not under
                        screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                        screen.blit(enemy_status_bar_backdrop.surf, enemy_status_bar_backdrop.rect)
                        try:
                            screen.blit(enemy.health_bar.surf, enemy.health_bar.rect)
                        except TypeError:
                            pass
                        screen.blit(enemy_status.surf, enemy_status.rect)
                        screen.blit(message_box.surf, message_box.rect)
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)

                        player_info_and_ui_updates()

                        # get current enemy name and create surf and rectangle to draw to screen
                        text_enemy_name_surf = font.render(str(enemy.name), True, "black", "light yellow")
                        text_enemy_name_rect = text_enemy_name_surf.get_rect()
                        text_enemy_name_rect.center = (800, 680)
                        screen.blit(text_enemy_name_surf, text_enemy_name_rect)
                        # get current enemy level and create surf and rectangle to draw to screen
                        text_enemy_level_surf = font.render(str(enemy.level), True, "black", "light yellow")
                        text_enemy_level_rect = text_enemy_level_surf.get_rect()
                        text_enemy_level_rect.center = (915, 680)
                        screen.blit(text_enemy_level_surf, text_enemy_level_rect)

                # after enemy is defeated, it may return a none type for collision. in this case, just ignore error
                except AttributeError:
                    pass

                # combat didn't happen this iteration, reset sprites to default surface image
                if not combat_happened:
                    if player.race == "amuna":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_amuna_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_amuna_battle)
                        if player.role == "fighter":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_fighter_amuna_battle)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_amuna_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_amuna_battle)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_amuna_battle)
                    if player.race == "sorae":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_sorae_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_sorae_battle)
                        if player.role == "fighter":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_fighter_sorae_battle)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_sorae_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sorae_battle)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_sorae_battle)
                    if player.race == "nuldar":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_nuldar_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_nuldar_battle)
                        if player.role == "fighter":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_fighter_nuldar_battle)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_nuldar_battle)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_nuldar_battle)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_nuldar_battle)
                    # --------------------------------------------------------------------------------------------------
                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                               snake_battle_sprite.y_coordinate,
                                               snake_battle)
                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                               ghoul_battle_sprite.y_coordinate,
                                               ghoul_battle)

                    pygame.display.flip()
                    combat_cooldown = False

                # combat happened this turn, update sprites for battle and apply short cooldown to attack again
                if combat_happened:
                    if player.race == "amuna":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_amuna_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_amuna_attack)
                        if not hard_strike:
                            if player.role == "fighter":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_fighter_amuna_attack)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_amuna_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_amuna_attack)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_amuna_attack)
                    if player.race == "sorae":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_sorae_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_sorae_attack)
                        if not hard_strike:
                            if player.role == "fighter":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_fighter_sorae_attack)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_sorae_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sorae_attack)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_sorae_attack)
                    if player.race == "nuldar":
                        if player.role == "mage":
                            if barrier_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_barrier_nuldar_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_mage_nuldar_attack)
                        if not hard_strike:
                            if player.role == "fighter":
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_fighter_nuldar_attack)
                        if player.role == "scout":
                            if sharp_sense_active:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_sense_nuldar_attack)
                            else:
                                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                            player_battle_sprite.y_coordinate,
                                                            player_scout_nuldar_attack)
                        if player.role == "":
                            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                                        player_battle_sprite.y_coordinate,
                                                        player_no_role_nuldar_attack)
                    # --------------------------------------------------------------------------------------------------
                    snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                               snake_battle_sprite.y_coordinate,
                                               snake_attack)
                    ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                               ghoul_battle_sprite.y_coordinate,
                                               ghoul_attack)

                    # flip to display ----------------------------------------------------------------------------------
                    # needs to flip here to show the new attacking sprites for the 1-second duration
                    pygame.display.flip()
                    combat_cooldown = True
                    # when combat happens, wait after flipping display to allow animation time to show
                    # 1000 milliseconds = 1 second
                    pygame.time.wait(1000)
                    # reset combat animation and ability to click without delay on next iteration
                    combat_happened = False
                    # reset hard strike condition so regular fighter attack animation resumes
                    hard_strike = False

            # ----------------------------------------------------------------------------------------------------------
            # if player is in shop -------------------------------------------------------------------------------------
            if in_shop:

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    elif event.type == QUIT:
                        exit()
                    shop = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "shop":
                        # if player has just started shop scenario, clear message box
                        if not encounter_started:
                            info_text_1 = "Click an inventory item to sell it."
                            info_text_2 = "Or, click buy button to buy an item."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                            # reset items bought condition on new shop encounter so that message is shown to
                            # player that they can click to buy or sell items.
                            item_bought = False
                            item_sold = False
                        # get which button player pressed during shop scenario (buy or leave)---------------------------
                        shop_button = click_handlers.shop_event_button(event, buy_button, leave_button)
                        if shop_button == "buy":
                            # if player hasn't bought an item yet, show message that item can be clicked to buy
                            if not item_bought:
                                info_text_1 = "Click an item to buy."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                            # if user clicks buy button again, set condition to false which will hide buy window
                            if buy_clicked:
                                buy_clicked = False
                                # remove buy window from display and clear temporary list used to populate it
                                if len(buy_shop_elements) > 0:
                                    buy_shop_elements.pop(0)
                                    shopkeeper_items.clear()

                            # user clicked buy button for the first time. show buy window ------------------------------
                            else:
                                buy_clicked = True
                                buy_shop_elements.insert(0, buy_inventory)
                                # if shopkeeper has items in their inventory
                                if len(npc_amuna_shopkeeper.items) > 0:
                                    buy_first_coord = 810
                                    buy_second_coord = 435

                                    # ----------------------------------------------------------------------------------
                                    buy_inventory_counter = 0
                                    # go through shop items and assign inventory slots (coordinates) to them
                                    for shop_item in npc_amuna_shopkeeper.items:
                                        if shop_item.name == "health potion":
                                            shop_item.update(buy_first_coord, buy_second_coord, health_pot_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "energy potion":
                                            shop_item.update(buy_first_coord, buy_second_coord, energy_pot_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic staff":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_staff_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic sword":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_sword_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic bow":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_bow_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic robes":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_robes_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic armor":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_armor_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1
                                        if shop_item.name == "basic tunic":
                                            shop_item.update(buy_first_coord, buy_second_coord, basic_tunic_img)
                                            shopkeeper_items.append(shop_item)
                                            buy_inventory_counter += 1

                                        buy_first_coord += 60
                                        if buy_inventory_counter > 3:
                                            buy_second_coord += 60
                                            buy_first_coord = 810
                                            buy_inventory_counter = 0
                        # ----------------------------------------------------------------------------------------------
                        # if player chooses to leave shop, set conditions to allow normal gameplay loop
                        if shop_button == "leave":
                            if len(buy_shop_elements) > 0:
                                buy_shop_elements.pop(0)
                                shopkeeper_items.clear()

                            buy_clicked = False
                            movement_able = True
                            interacted = False
                            encounter_started = False
                            in_shop = False
                            in_over_world = True

                        # ----------------------------------------------------------------------------------------------
                        # shop click handlers --------------------------------------------------------------------------
                        if buy_clicked:
                            buy_item = click_handlers.buy_event_item(event, shopkeeper_items)
                            try:
                                # player has clicked health potion. If player has enough rupees it will buy item
                                # and add to their inventory. Also subtracts the price from current rupee count
                                if buy_item.name == "health potion":
                                    if len(player.items) < 16:
                                        if player.rupees > 9:
                                            info_text_1 = "You Bought Health Potion for 10 rupees."
                                            info_text_2 = "Health Potion added to inventory."
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.rupees = player.rupees - 10
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Health Potion cost 10 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "energy potion":
                                    if len(player.items) < 16:
                                        if player.rupees > 9:
                                            info_text_1 = "Bought Energy Potion for 10 rupees."
                                            info_text_2 = "Energy Potion added to inventory."
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                            player.rupees = player.rupees - 10
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Energy Potion cost 10 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic staff":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Staff for 20 rupees."
                                            info_text_2 = "Basic Staff added to inventory."
                                            player.items.append(Item("basic staff", "mage", 200, 200,
                                                                     basic_staff_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Staff cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic sword":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Sword for 20 rupees."
                                            info_text_2 = "Basic Sword added to inventory."
                                            player.items.append(Item("basic sword", "fighter", 200, 200,
                                                                     basic_sword_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Sword cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic bow":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Bow for 20 rupees."
                                            info_text_2 = "Basic Bow added to inventory."
                                            player.items.append(Item("basic bow", "scout", 200, 200,
                                                                     basic_bow_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Bow cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic robes":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Robes for 20 rupees."
                                            info_text_2 = "Basic Robes added to inventory."
                                            player.items.append(Item("basic robes", "mage", 200, 200,
                                                                     basic_robes_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Robes cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic armor":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Armor for 20 rupees."
                                            info_text_2 = "Basic Armor added to inventory."
                                            player.items.append(Item("basic armor", "fighter", 200, 200,
                                                                     basic_armor_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Armor cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                                if buy_item.name == "basic tunic":
                                    if len(player.items) < 16:
                                        if player.rupees > 19:
                                            info_text_1 = "Bought Basic Tunic for 20 rupees."
                                            info_text_2 = "Basic Tunic added to inventory."
                                            player.items.append(Item("basic tunic", "scout", 200, 200,
                                                                     basic_tunic_img))
                                            player.rupees = player.rupees - 20
                                            item_bought = True
                                        else:
                                            info_text_1 = "You do not have enough rupees."
                                            info_text_2 = "Basic Tunic cost 20 rupees."
                                    else:
                                        info_text_1 = "Your inventory is full."
                                        info_text_2 = ""
                            except AttributeError:
                                pass

                        # handles selling items when clicked
                        sell_item = click_handlers.sell_event_item(event)
                        try:
                            # player has clicked health potion. This will sell the item, removing it from
                            # inventory and giving them "x" rupees to add to their current count
                            if sell_item.name == "health potion":
                                info_text_1 = "Sold Health Potion for 5 rupees."
                                info_text_2 = "Health Potion removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "energy potion":
                                info_text_1 = "Sold Energy Potion for 5 rupees."
                                info_text_2 = "Energy Potion removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "shiny rock":
                                info_text_1 = "Sold Shiny Rock for 5 rupees."
                                info_text_2 = "Shiny Rock removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "bone dust":
                                info_text_1 = "Sold Bone Dust for 10 rupees."
                                info_text_2 = "Bone Dust removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 10
                                item_sold = True
                            if sell_item.name == "basic staff":
                                info_text_1 = "Sold Basic Staff for 5 rupees."
                                info_text_2 = "Basic Staff removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic sword":
                                info_text_1 = "Sold Basic Sword for 5 rupees."
                                info_text_2 = "Basic Sword removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic bow":
                                info_text_1 = "Sold Basic Bow for 5 rupees."
                                info_text_2 = "Basic Bow removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic robes":
                                info_text_1 = "Sold Basic Robes for 5 rupees."
                                info_text_2 = "Basic Robes removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic armor":
                                info_text_1 = "Sold Basic Armor for 5 rupees."
                                info_text_2 = "Basic Armor removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "basic tunic":
                                info_text_1 = "Sold Basic Tunic for 5 rupees."
                                info_text_2 = "Basic Tunic removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                player.rupees = player.rupees + 5
                                item_sold = True
                            if sell_item.name == "temporary item":
                                info_text_1 = "Sold Temporary Item for 0 rupees."
                                info_text_2 = "Temporary Item removed from inventory."
                                player.items.remove(sell_item)
                                drawing_functions.player_items.remove(sell_item)
                                item_sold = True
                        except AttributeError:
                            pass

                # outside of shop event loop ---------------------------------------------------------------------------
                # draw objects to screen related to shop scenario
                if building.name == "shop":
                    if player.current_zone == "seldon":
                        screen.blit(seldon_district_shop, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(buy_button.surf, buy_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)

                        player_info_and_ui_updates()

                        if buy_clicked:
                            for window in buy_shop_elements:
                                screen.blit(window.surf, window.rect)
                            # get item from shopkeeper's inventory and draw with buy window
                            for shop_item in shopkeeper_items:
                                screen.blit(shop_item.surf, shop_item.rect)

            # ----------------------------------------------------------------------------------------------------------
            # if player is in inn
            if in_inn:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                    inn = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "inn":
                        # if player has just started inn scenario, clear message box
                        if not encounter_started:
                            info_text_1 = "Click rest button to sleep."
                            info_text_2 = "Sleep regains health and energy."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                        # get which button player pressed during inn scenario (rest or leave)
                        inn_button = click_handlers.inn_event_button(event, rest_button, leave_button)
                        if inn_button == "rest":
                            # if player has not yet rested this instance
                            if not rested:
                                rest_clicked = True
                                info_text_1 = "You feel well rested."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                            # if player has already rested this instance
                            else:
                                info_text_1 = "You've already rested."
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""

                    # if player chooses to leave shop, set conditions to allow normal gameplay loop
                    if inn_button == "leave":
                        rest_clicked = False
                        movement_able = True
                        interacted = False
                        encounter_started = False
                        in_inn = False
                        in_over_world = True
                        # reset rest condition and screen fade effect so next instance player can rest again
                        rested = False
                        faded_inn_screen = False

                # outside of inn event loop ----------------------------------------------------------------------------
                # if building is an inn in the seldon zone
                if building.name == "inn":
                    if player.current_zone == "seldon":
                        # if player has just rested, fade inn screen back in with alpha value loop
                        if rested:
                            # so this only happens once and not each iteration
                            if not faded_inn_screen:
                                for alpha in range(0, 50):
                                    seldon_district_inn.set_alpha(alpha)
                                    screen.blit(seldon_district_inn, (0, 0))
                                    pygame.display.flip()
                                faded_inn_screen = True
                            else:
                                seldon_district_inn.set_alpha(255)
                                screen.blit(seldon_district_inn, (0, 0))
                        if not rested:
                            seldon_district_inn.set_alpha(255)
                            screen.blit(seldon_district_inn, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(rest_button.surf, rest_button.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(message_box.surf, message_box.rect)

                    player_info_and_ui_updates()

                    # --------------------------------------------------------------------------------------------------
                    if rest_clicked:
                        if not rested:
                            # set sleep screen to fade in with alpha value loop. Flip each iteration to show
                            for alpha in range(0, 255):
                                nera_sleep_screen.set_alpha(alpha)
                                screen.blit(nera_sleep_screen, (0, 0))
                                # flip sleep screen to display each iteration to show fade
                                pygame.display.flip()
                            player.health = 100
                            player.energy = 100
                            rested = True

            # ----------------------------------------------------------------------------------------------------------
            # if player is in academia
            if in_academia:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                    academia = pygame.sprite.spritecollideany(player, buildings)
                    if building.name == "academia":
                        if not encounter_started:
                            info_text_1 = "Click a book to view skills."
                            info_text_2 = "Then, click a skill to learn it."
                            info_text_3 = ""
                            info_text_4 = ""
                            encounter_started = True
                        # get which button player pressed during academia scenario (learn or leave)
                        academia_button = click_handlers.academia_event_button(event, mage_learn_button,
                                                                               fighter_learn_button,
                                                                               scout_learn_button,
                                                                               leave_button)
                        if academia_button == "mage learn":
                            mage_learn_clicked = True
                        if academia_button == "fighter learn":
                            fighter_learn_clicked = True
                        if academia_button == "scout learn":
                            scout_learn_clicked = True

                    # if player chooses to leave academia, set conditions to allow normal gameplay loop
                    if academia_button == "leave":
                        learn_clicked = False
                        movement_able = True
                        interacted = False
                        encounter_started = False
                        in_academia = False
                        in_over_world = True
                        mage_learn_clicked = False
                        fighter_learn_clicked = False
                        scout_learn_clicked = False
                        learned = False
                        books.clear()
                        skill_learn_items.clear()

                    # get which button player pressed during book skill open (skill or close)
                    book_button = click_handlers.skill_learn_event_item(event, skill_learn_items)
                    if mage_learn_clicked:
                        try:
                            if book_button.name == "barrier learn button":
                                if not barrier_learned:
                                    if player.knowledge["mage"] > 39:
                                        player.skills_mage["skill 2"] = "barrier"
                                        info_text_1 = "'Barrier' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["mage"] -= 40
                                        barrier_learned = True
                                    else:
                                        info_text_1 = "40 mage knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Barrier'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                mage_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass
                    if fighter_learn_clicked:
                        try:
                            if book_button.name == "hard strike learn button":
                                if not hard_strike_learned:
                                    if player.knowledge["fighter"] > 39:
                                        player.skills_fighter["skill 2"] = "hard strike"
                                        info_text_1 = "'Hard Strike' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["fighter"] -= 40
                                        hard_strike_learned = True
                                    else:
                                        info_text_1 = "40 fighter knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Hard Strike'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                fighter_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass
                    if scout_learn_clicked:
                        try:
                            if book_button.name == "sharp sense learn button":
                                if not sharp_sense_learned:
                                    if player.knowledge["scout"] > 39:
                                        player.skills_scout["skill 2"] = "sharp sense"
                                        info_text_1 = "'Sharp Sense' skill learned!"
                                        info_text_2 = "Skill added. 40 knowledge used."
                                        player.knowledge["scout"] -= 40
                                        sharp_sense_learned = True
                                    else:
                                        info_text_1 = "40 scout knowledge required to learn."
                                else:
                                    info_text_1 = "You've already learned 'Sharp Sense'."
                                    info_text_2 = ""
                            if book_button.name == "close button":
                                scout_learn_clicked = False
                                books.clear()
                                skill_learn_items.clear()
                        except AttributeError:
                            pass

                # outside of inn event loop ----------------------------------------------------------------------------
                # draw objects to screen related to academia scenario
                if building.name == "academia":
                    if player.current_zone == "seldon":
                        screen.blit(seldon_district_academia, (0, 0))
                        screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                        screen.blit(hp_bar.surf, hp_bar.rect)
                        screen.blit(en_bar.surf, en_bar.rect)
                        screen.blit(xp_bar.surf, xp_bar.rect)
                        screen.blit(mage_learn_button.surf, mage_learn_button.rect)
                        screen.blit(fighter_learn_button.surf, fighter_learn_button.rect)
                        screen.blit(scout_learn_button.surf, scout_learn_button.rect)
                        screen.blit(leave_button.surf, leave_button.rect)
                        screen.blit(message_box.surf, message_box.rect)
                    player_info_and_ui_updates()
                    for book in books:
                        screen.blit(book.surf, book.rect)
                    for skill_item in skill_learn_items:
                        screen.blit(skill_item.surf, skill_item.rect)

                    screen.blit(knowledge_window.surf, knowledge_window.rect)
                    text_mage_knowledge_surf = font.render(str(player.knowledge["mage"]), True, "black",
                                                           "light yellow")
                    text_mage_knowledge_rect = text_mage_knowledge_surf.get_rect()
                    text_mage_knowledge_rect.center = (515, 680)
                    screen.blit(text_mage_knowledge_surf, text_mage_knowledge_rect)
                    text_fighter_knowledge_surf = font.render(str(player.knowledge["fighter"]), True, "black",
                                                              "light yellow")
                    text_fighter_knowledge_rect = text_fighter_knowledge_surf.get_rect()
                    text_fighter_knowledge_rect.center = (695, 680)
                    screen.blit(text_fighter_knowledge_surf, text_fighter_knowledge_rect)
                    text_scout_knowledge_surf = font.render(str(player.knowledge["scout"]), True, "black",
                                                            "light yellow")
                    text_scout_knowledge_rect = text_scout_knowledge_surf.get_rect()
                    text_scout_knowledge_rect.center = (865, 680)
                    screen.blit(text_scout_knowledge_surf, text_scout_knowledge_rect)

                    # --------------------------------------------------------------------------------------------------
                    if mage_learn_clicked and fighter_learn_clicked is False and scout_learn_clicked is False:
                        books.append(mage_book)
                        skill_learn_items.append(barrier_learn_button)
                        skill_learn_items.append(close_button)
                    if fighter_learn_clicked and mage_learn_clicked is False and scout_learn_clicked is False:
                        books.append(fighter_book)
                        skill_learn_items.append(hard_strike_learn_button)
                        skill_learn_items.append(close_button)
                    if scout_learn_clicked and fighter_learn_clicked is False and mage_learn_clicked is False:
                        books.append(scout_book)
                        skill_learn_items.append(sharp_sense_learn_button)
                        skill_learn_items.append(close_button)

            # ----------------------------------------------------------------------------------------------------------
            # if player interacting with an npc (quest) ----------------------------------------------------------------
            if in_npc_interaction:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                    if level_up_win.rect.collidepoint(pos):
                        drawing_functions.level_up_draw(level_up_win, player, font, False)
                    npc = pygame.sprite.spritecollideany(player, npcs)
                    if npc:
                        if interacted:
                            movement_able = False
                            if not encounter_started:
                                info_text_1 = ""
                                info_text_2 = ""
                                info_text_3 = ""
                                info_text_4 = ""
                                encounter_started = True

                            # npc was interacted with, if quest button clicked get npc name and check quest progress
                            npc_button = npc_event_button(event)
                            if npc_button == "quest":
                                # garan npc, check player's quest progress and reward if completed
                                if npc.name == "garan":
                                    if player.quest_progress["sneaky snakes"] == 4 and not \
                                            player.quest_complete["sneaky snakes"]:

                                        if len(player.items) < 16:
                                            player.quest_complete["sneaky snakes"] = True
                                            player.current_quests["sneaky snakes"] = "You completed this quest!"
                                            info_text_1 = "You've completed Garan's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "2 health and energy potions. "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                gameplay_functions.level_up(player)
                                            player.reputation["amuna"] += 10
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.items.append(Item("health potion", "potion", 200, 200,
                                                                     health_pot_img))
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                            player.items.append(Item("energy potion", "potion", 200, 200,
                                                                     energy_pot_img))
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["sneaky snakes"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                                # maurelle npc, check player's quest progress and reward if completed
                                if npc.name == "maurelle":
                                    if player.quest_progress["village repairs"] == 4 and not \
                                            player.quest_complete["village repairs"]:
                                        if len(player.items) < 16:
                                            player.quest_complete["village repairs"] = True
                                            player.current_quests["village repairs"] = "You completed this quest!"
                                            info_text_1 = "You've completed Maurelle's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "Nera's blessing (Trinket). "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                gameplay_functions.level_up(player)
                                            player.reputation["amuna"] += 10
                                            player.items.append(Item("temporary item", "trinket", 200, 200, temp_img))
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["village repairs"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                                # guard npc, check player's quest progress and reward if completed
                                if npc.name == "guard":
                                    if player.quest_progress["ghouled again"] == 4 and not \
                                            player.quest_complete["ghouled again"]:

                                        if len(player.items) < 16:
                                            player.quest_complete["ghouled again"] = True
                                            player.current_quests["ghouled again"] = "You completed this quest!"
                                            info_text_1 = "You've completed Guard's quest!"
                                            info_text_2 = "You've gained: "
                                            info_text_3 = "Rohir bridge gate access. "
                                            info_text_4 = "50 xp and 10 amuna rep. "
                                            player.experience += 50
                                            if player.experience >= 100:
                                                gameplay_functions.level_up(player)
                                            player.reputation["amuna"] += 10
                                        else:
                                            info_text_1 = "You completed the quest, but "
                                            info_text_2 = "Your inventory is full!"

                                    if not quest_clicked:
                                        if not player.quest_complete["ghouled again"]:
                                            drawing_functions.quest_box_draw(npc, True, garan_quest_window,
                                                                             maurelle_quest_window,
                                                                             guard_quest_window,
                                                                             accept_button, decline_button)
                                            quest_clicked = True
                                        else:
                                            info_text_1 = "You've completed this quest!"
                                    else:
                                        drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                         maurelle_quest_window, guard_quest_window,
                                                                         accept_button, decline_button)
                                        quest_clicked = False

                            # in quest window pop-up, if accept or decline buttons are clicked
                            quest_buttons = quest_event_button(event)
                            if quest_buttons == "accept":
                                info_text_1 = "You've accepted the quest!"
                                if npc.name == "garan":
                                    # when players first accept garan's quest he will give them a basic weapon
                                    if not npc.gift:
                                        player.items.append(Item("basic staff", "mage", 200, 200,
                                                                 basic_staff_img))
                                        player.items.append(Item("basic sword", "fighter", 200, 200,
                                                                 basic_sword_img))
                                        player.items.append(Item("basic bow", "scout", 200, 200,
                                                                 basic_bow_img))
                                        player.rupees += 20
                                        info_text_2 = "garan has given you:"
                                        info_text_3 = "Basic Staff, Basic Sword, Basic Bow"
                                        info_text_4 = "And 20 rupees!"
                                        npc.gift = True

                                    player.quest_status["sneaky snakes"] = True
                                    player.current_quests["sneaky snakes"] = "Garan asked you to defeat" \
                                                                             " snakes near the river."
                                if npc.name == "maurelle":
                                    player.quest_status["village repairs"] = True
                                    player.current_quests["village repairs"] = "Maurelle asked you to " \
                                                                               "gather lumber from nearby trees."
                                if npc.name == "guard":
                                    player.quest_status["ghouled again"] = True
                                    player.current_quests["ghouled again"] = "The Guard asked you to defeat" \
                                                                             " ghouls nearby the Castle wall."
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)
                            # if player chooses to decline, just close the quest window
                            if quest_buttons == "decline":
                                info_text_1 = ""
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)
                            if npc_button == "leave":
                                movement_able = True
                                interacted = False
                                encounter_started = False
                                in_npc_interaction = False
                                in_over_world = True
                                quest_clicked = False
                                drawing_functions.quest_box_draw(npc, False, garan_quest_window,
                                                                 maurelle_quest_window, guard_quest_window,
                                                                 accept_button, decline_button)

                # outside npc interaction event loop -------------------------------------------------------------------
                # draw objects to screen related to npc scenario
                if player.current_zone == "seldon":
                    # create blank background to be drawn on top of each iteration
                    screen.fill((255, 255, 255))  # (255, 255, 255) RGB value for WHITE
                    screen.blit(seldon_district_battle, (0, 0))
                    screen.blit(status_bar_backdrop.surf, status_bar_backdrop.rect)
                    screen.blit(hp_bar.surf, hp_bar.rect)
                    screen.blit(en_bar.surf, en_bar.rect)
                    screen.blit(xp_bar.surf, xp_bar.rect)
                    screen.blit(player_battle_sprite.surf, player_battle_sprite.rect)
                    screen.blit(message_box.surf, message_box.rect)
                    screen.blit(leave_button.surf, leave_button.rect)
                    screen.blit(quest_button.surf, quest_button.rect)
                    screen.blit(npc_name_plate.surf, npc_name_plate.rect)
                    if npc.name == "garan":
                        screen.blit(npc_garan_interaction.surf, npc_garan_interaction.rect)
                    if npc.name == "maurelle":
                        screen.blit(npc_maurelle_interaction.surf, npc_maurelle_interaction.rect)
                    if npc.name == "guard":
                        screen.blit(npc_guard_interaction.surf, npc_guard_interaction.rect)

                    player_info_and_ui_updates()

                    # get current npc name and create surf and rectangle to draw to screen
                    text_npc_name_surf = font.render(str(npc.name), True, "black", "light yellow")
                    text_npc_name_rect = text_npc_name_surf.get_rect()
                    text_npc_name_rect.center = (640, 192)
                    screen.blit(text_npc_name_surf, text_npc_name_rect)
                    drawing_functions.draw_it(screen)

            # ----------------------------------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------------------------------
            # if player is in korlok over world
            if player.current_zone == "korlok" and in_over_world:
                screen.blit(korlok_district_bg, (0, 0))

                rohir_gate.update(525, 600, pygame.image.load(resource_urls.rohir_gate).convert())
                screen.blit(rohir_gate.surf, rohir_gate.rect)

                # hearth button is clicked, sets fade transition for hearth screen and then back to district bg --------
                if hearth_clicked:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 200):
                        seldon_hearth_screen.set_alpha(alpha)
                        screen.blit(seldon_hearth_screen, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    hearth_clicked = False
                    hearthed = True
                if hearthed:
                    screen.fill((0, 0, 0))
                    for alpha in range(0, 50):
                        seldon_district_bg.set_alpha(alpha)
                        screen.blit(seldon_district_bg, (0, 0))
                        # flip sleep screen to display each iteration to show fade
                        pygame.display.flip()
                    seldon_district_bg.set_alpha(255)
                    screen.blit(seldon_district_bg, (0, 0))
                    pygame.display.flip()
                    hearthed = False
                    info_text_1 = "You recalled to the hearth stone."
                # ------------------------------------------------------------------------------------------------------

                player_info_and_ui_updates()

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            exit()
                        if event.key == K_f:
                            if pygame.sprite.spritecollideany(player, most_sprites):
                                interacted = True
                    elif event.type == QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if hearth_button.rect.collidepoint(pos):
                            hearth_clicked = True
                            player.current_zone = "seldon"
                            player.x_coordinate = 850
                            player.y_coordinate = 650
                        if save_button.rect.collidepoint(pos):
                            try:
                                with open("save_game", "rb") as f:
                                    saved = True
                            except FileNotFoundError:
                                saved = False
                                pass
                            if saved:
                                save_check_window.append(save_check)
                                save_check_window.append(yes_button)
                                save_check_window.append(no_button)
                            if not saved:
                                save_game()
                                saved = True
                                info_text_1 = "You saved your game. "
                        if yes_button.rect.collidepoint(pos):
                            save_game()
                            save_check_window.clear()
                            info_text_1 = "You saved your game. "
                        if no_button.rect.collidepoint(pos):
                            save_check_window.clear()

                        if character_button.rect.collidepoint(pos):
                            if character_button_clicked:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, False)
                                character_button_clicked = False
                            else:
                                drawing_functions.character_sheet_info_draw(character_sheet, player, font, True)
                                character_button_clicked = True
                        if journal_button.rect.collidepoint(pos):
                            if journal_button_clicked:
                                drawing_functions.journal_info_draw(journal, player, font, False)
                                journal_button_clicked = False
                            else:
                                drawing_functions.journal_info_draw(journal, player, font, True)
                                journal_button_clicked = True

                        if level_up_win.rect.collidepoint(pos):
                            drawing_functions.level_up_draw(level_up_win, player, font, False)

                    # --------------------------------------------------------------------------------------------------
                    quest_item = pygame.sprite.spritecollideany(player, quest_items)
                    try:
                        if quest_item.name == "rohir gate":
                            if player.quest_complete["ghouled again"]:
                                info_text_1 = f"Press 'F' key to enter Seldon District."
                                if interacted:
                                    player.current_zone = "seldon"
                                    in_over_world = True
                                    interacted = False
                                    rohir_gate.update(525, 40, pygame.image.load(resource_urls.rohir_gate).convert())
                    except AttributeError:
                        pass

                    # click handlers -----------------------------------------------------------------------------------
                    inventory_event = click_handlers.inventory_click_handler(player, event,
                                                                             player_mage_amuna_down_1,
                                                                             player_mage_nuldar_down_1,
                                                                             player_mage_sorae_down_1,
                                                                             player_fighter_amuna_down_1,
                                                                             player_fighter_nuldar_down_1,
                                                                             player_fighter_sorae_down_1,
                                                                             player_scout_amuna_down_1,
                                                                             player_scout_nuldar_down_1,
                                                                             player_scout_sorae_down_1)
                    if inventory_event["item message"] != "":
                        info_text_1 = inventory_event["item message"]
                        info_text_2 = ""
                    # function to handle equipment item clicks. apply item message to message box if not empty str.
                    equipment_event = click_handlers.equipment_click_handler(player, event,
                                                                             player_no_role_amuna_down_1,
                                                                             player_no_role_nuldar_down_1,
                                                                             player_no_role_sorae_down_1)
                    if equipment_event["equipment message"] != "":
                        info_text_1 = equipment_event["equipment message"]
                        info_text_2 = ""

                # outside of event loop --------------------------------------------------------------------------------
                walking_return_korlok = walk_time(walk_tic)
                if walking_return_korlok["reset"]:
                    walk_tic = time.perf_counter()
                if movement_able:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                        player.update("right", "korlok", walking_return_korlok["total time"])
                    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                        player.update("left", "korlok", walking_return_korlok["total time"])
                    if pressed_keys[K_w] or pressed_keys[K_UP]:
                        player.update("up", "korlok", walking_return_korlok["total time"])
                    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                        player.update("down", "korlok", walking_return_korlok["total time"])

            # end of whole iteration -----------------------------------------------------------------------------------
            pygame.display.flip()
            # 60 frames per second game rate ---------------------------------------------------------------------------
            clock.tick(60)

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # player has died, show game over and give continue option
        else:
            # draw game over screen and continue button
            screen.blit(game_over_screen, (0, 0))
            screen.blit(lets_go_button.surf, lets_go_button.rect)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    # player chooses to continue, reset character experience and half health and energy on respawn
                    if lets_go_button.rect.collidepoint(pos):
                        movement_able = True
                        # reset interaction, so it doesn't immediately interact again on subsequent collisions
                        interacted = False
                        # make sure that windows haven't registered a click on reset for whatever reason
                        inventory_clicked = False
                        sell_clicked = False
                        buy_clicked = False
                        encounter_started = False
                        in_battle = False
                        in_over_world = True
                        # turn off barrier and restore original defence if player mage was killed while active
                        if barrier_active:
                            barrier_active = False
                            player.defence = original_defence
                        # turn off barrier and restore original defence if player mage was killed while active
                        if sharp_sense_active:
                            sharp_sense_active = False
                            player.offense = original_offense

                        if player.current_zone == "nascent":
                            player.x_coordinate = 760
                            player.y_coordinate = 510
                            player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                        if player.current_zone == "seldon":
                            player.x_coordinate = 425
                            player.y_coordinate = 690
                            player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                        if player.current_zone == "korlok":
                            player.x_coordinate = 500
                            player.y_coordinate = 500
                            player.rect = player.surf.get_rect(center=(player.x_coordinate, player.y_coordinate))
                        player.health = 50
                        player.energy = 50

                        # bring enemies back to full health
                        for enemy in enemies:
                            enemy.health = 100
                            enemy.health_bar.update(enemy.health_bar.x_coordinate, enemy.health_bar.y_coordinate,
                                                    health_bar_update(enemy))
                        player.alive_status = True
                elif event.type == QUIT:
                    exit()
            pygame.display.flip()

# related to music - implement later
# we can stop and quit the mixer
# pygame.mixer.music.stop()
# pygame.mixer.quit()
