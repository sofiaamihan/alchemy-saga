from tkinter import *
from scripts.characters import *

clicked_buttons = []
user_player = None
comp_enemy = None
user_player2 = None
comp_enemy2 = None
next_move = False
number_of_enemies = IntVar()
comp_enemy_choice = ""
net_attack = 0
turns = 0
rounds = 1
battling = True
choosing_action = True
choosing_skill = True
enemy_defense = 0
enemy2_defense = 0
player_defense = 0
player2_defense = 0
stats = StringVar()
stats2 = StringVar()
stats3 = StringVar()
stats4 = StringVar()
round_num = StringVar()
screen5_frame = None
screen6_frame = None
content = None

def restart_variables():
    """Restarts all the necessary variables."""
    global turns, rounds, enemy_defense, player_defense, next_move, LIST_OF_CHARACTERS
    next_move = False
    turns = 0
    rounds = 1
    enemy_defense = 0
    player_defense = 0
    for character in LIST_OF_CHARACTERS:
        character.restart()