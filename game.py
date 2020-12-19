import tkinter as tk
import pynput as pn
import random as rand

# Planning:
# 1. Game controls
# - Game uses WASD plus spacebar and arrow keys
# 2. Game mechanics
# - Game has Inert, Active, Bomb, Deploy, and Boss types of enemies
# - each enemy has a random chance to spawn
# 3. Scoreboard
# - Game should show lives left, specials left, score, highest score.
# When the game ends, some processing should be done.
# The game should record the current score and append it to the score list.
# The game should then sort the list by numerical value and compare the largest item to the highscore.
# If it is larger, the highscore will update.
# The game should also reset to initial values (3 lives, 0 specials)
lives_left = 3
specials_left = 0
score = 0
score_list = []
highscore = 0
score_per_enemy = []
enemy_killed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
key_input = ""

class SpaceShip:
    def __init__(self, lives_left, specials_left, score, highscore, score_list, position_x, position_y):
        self.lives = lives_left
        self.specials = specials_left
        self.score = score
        self.highscore = highscore
        self.score_list = score_list
        self.position = [position_x, position_y]
    def lose_life(self, lives):
        self.lives -= 1
    def reset(self, lives, specials):
        self.lives = 3
        self.specials = 0
        # reset scoreboard
    def gain_special(self, specials):
        self.specials += 1
        # animate specialcounter
    def use_special(self, specials):
        self.specials -= 1
        # animate special attack
    def gain_score(self, score, highscore, enemy_killed):
        self.score += score_per_enemy[enemy_killed]
        self.score_list.append(self.score)
        highscore = max(self.score_list)
    def move(self, key_input):
        if key_input == "w" or key_input == "W":
            # Move forwards
            pass
        elif key_input == "s" or key_input == "S":
            # Move backwards
            pass
        elif key_input == "a" or key_input == "A":
            # Move left
            pass
        elif key_input == "d" or key_input == "D":
            # Move right
            pass
    def shoot(self):
        # Shooting animation
        pass
    def use_special(self):
        #special attack animation
        pass
class Inert:
    def __init__(self, type, health):
        self.type = ["T1", "T2", "T3"]
        self.health = health
    def death_inert(self):
        # remove
        pass
    def spawn(self, type):
        # spawn in an Inert
        spawn_type = type[rand.randint(0, 3)]
    def move_inert(self):
        #move towards the player
        pass
