# ----------IMPORTS----------
from tkinter import *
screen1 = Tk()

import random
from PIL import Image, ImageTk
from scripts.constants import *
from scripts.characters import *
from scripts.photos import *
from scripts.functions import * 
from scripts.variables import *

# ----------SCREEN 1----------
screen1.geometry(POSITION)
screen1.title("Sofia Project 1B: Turn-Based RPG")
screen1.config(bg=BG_COLOUR)
screen1.rowconfigure(0, weight=1)
screen1.columnconfigure(0, weight=1)
screen1_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
screen1_frame.grid(row=0, column=0)

# ----------FUNCTIONS (CREATING LAYERED SCREENS VIA FRAMES)----------
def back(widget):
    """Acts as a Back Button by Destroying Current Frame"""
    widget.destroy()


def battle_screen():
    """Displays Combat Screen"""
    global number_of_enemies, content, rounds, round_num, screen6_frame
    screen6_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
    for num in range(0, 2):
        screen6_frame.grid_columnconfigure(num, weight=1)
    screen6_frame.grid(row=0, column=0)
    screen6_frame.grid_propagate(False)

    def exit_battle():
        """Exits the Whole Game"""
        global next_move, choosing_action, battling
        next_move = False
        choosing_action = False
        battling = False
        warning = Toplevel(screen1, bg=FG_COLOUR)
        warning.geometry("250x50+600+400")
        warning.title("Exit Warning")
        warning_frame = Frame(warning, width=200, height=200, bg=FG_COLOUR)
        for numb_ in range(0, 2):
            warning_frame.rowconfigure(numb_, weight=1)
        warning.grid_propagate(False)
        warning_frame.pack()
        warning_text = Label(warning_frame, fg=BG_COLOUR, bg=FG_COLOUR, font=SMALL_FONT)
        warning_text.config(text="Are you sure you want to EXIT the game?")
        warning_text.grid(row=0, column=0, columnspan=2)

        def no_clicked():
            warning.destroy()

        def yes_clicked():
            screen1.destroy()
        no = Button(warning_frame, fg=FG_COLOUR, bg=BG_COLOUR, font=SMALL_FONT, text="No", command=no_clicked)
        no.config(width=5)
        no.grid(row=1, column=0)
        yes = Button(warning_frame, fg=FG_COLOUR, bg=BG_COLOUR, font=SMALL_FONT, text="Yes", command=yes_clicked)
        yes.config(width=5)
        yes.grid(row=1, column=1)

    def restart_battle():
        """Restarts the Whole Game"""
        global next_move, choosing_action, battling
        next_move = False
        choosing_action = False
        battling = False
        warning = Toplevel(screen1, bg=FG_COLOUR)
        warning.geometry("250x50+600+400")
        warning.title("Restart Warning")
        warning_frame = Frame(warning, width=240, height=200, bg=FG_COLOUR)
        for numb_ in range(0, 2):
            warning_frame.rowconfigure(numb_, weight=1)
        warning.grid_propagate(False)
        warning_frame.pack()
        warning_text = Label(warning_frame, fg=BG_COLOUR, bg=FG_COLOUR, font=SMALL_FONT)
        warning_text.config(text="Are you sure you want to RESTART the game?")
        warning_text.grid(row=0, column=0, columnspan=2)

        def no_clicked():
            warning.destroy()

        def yes_clicked():
            screen5_frame.destroy()
            screen6_frame.destroy()
            restart_variables()
            warning.destroy()

        no = Button(warning_frame, fg=FG_COLOUR, bg=BG_COLOUR, font=SMALL_FONT, text="No", command=no_clicked)
        no.config(width=5)
        no.grid(row=1, column=0)
        yes = Button(warning_frame, fg=FG_COLOUR, bg=BG_COLOUR, font=SMALL_FONT, text="Yes", command=yes_clicked)
        yes.config(width=5)
        yes.grid(row=1, column=1)

    def display_player_char():
        """Displays Player Characters on Combat Screen"""
        Label(image_frame, bg=BG_COLOUR, image=user_player.image).grid(column=0, row=0)
        if number_of_enemies.get() == 2:
            Label(image_frame, bg=BG_COLOUR, image=user_player2.image).grid(column=1, row=0)

    def display_enemy_char():
        """Displays Enemy Characters on Combat Screen"""
        Label(image_frame, bg=BG_COLOUR, image=comp_enemy.image).grid(column=4, row=0)
        if number_of_enemies.get() == 2:
            Label(image_frame, bg=BG_COLOUR, image=comp_enemy2.image).grid(column=3, row=0)

    def attack(attacker, defender):
        """Attack the Player/Enemy depending on Attacker/Defender Input."""
        global net_attack, content
        net_attack = attacker.ap - defender.dp
        insert_text(f"\n{attacker.name} is attacking...", content)
        insert_text(f"{attacker.name} has inflicted damage!", content)

    def defend(defender):
        """Defend the Player/Enemy permanently depending on Defender Input."""
        global player_defense, player2_defense, enemy_defense, enemy2_defense, content
        if defender == user_player:
            player_defense += 1
        if defender == user_player2:
            player2_defense += 1
        if defender == comp_enemy:
            enemy_defense += 1
        if defender == comp_enemy2:
            enemy2_defense += 1
        defender.dp *= 1.10
        defender.dp = int(defender.dp)
        insert_text(f"\n{defender.name} is defending...", content)
        insert_text(f"{defender.name}'s defense is up!", content)

    def display_psychic_buttons():
        """Displays Job Class:Psychic Buttons"""
        heal_button.pack(expand=True)
        aura_button.pack(expand=True)
        trick_button.pack(expand=True)

    def display_mineral_buttons():
        """Displays Job Class:Mineral Buttons"""
        boulder_brute_button.pack(expand=True)
        carbon_protect_button.pack(expand=True)
        pressurise_button.pack(expand=True)

    def display_lux_buttons():
        """Displays Job Class:Lux Buttons"""
        prismatic_beam_button.pack(expand=True)
        glimmer_button.pack(expand=True)
        illuminate_button.pack(expand=True)

    def enable_buttons(user):
        """Enables Buttons"""
        global player_defense
        attack_button['state'] = NORMAL
        if user == user_player:
            if player_defense < 4:
                defend_button['state'] = NORMAL
        if user == user_player2:
            if player2_defense < 4:
                defend_button['state'] = NORMAL
        if user == isla:
            display_psychic_buttons()
            if isla.mp > LIST_OF_SKILL_POINTS[0]:
                heal_button['state'] = NORMAL
            if isla.mp > LIST_OF_SKILL_POINTS[1]:
                aura_button['state'] = NORMAL
            if isla.mp > LIST_OF_SKILL_POINTS[2]:
                trick_button['state'] = NORMAL
        elif user == rosa:
            display_mineral_buttons()
            if rosa.mp > LIST_OF_SKILL_POINTS[3]:
                boulder_brute_button['state'] = NORMAL
            if rosa.mp > LIST_OF_SKILL_POINTS[4]:
                carbon_protect_button['state'] = NORMAL
            if rosa.mp > LIST_OF_SKILL_POINTS[5]:
                pressurise_button['state'] = NORMAL
        else:
            display_lux_buttons()
            if jess.mp > LIST_OF_SKILL_POINTS[6]:
                prismatic_beam_button['state'] = NORMAL
            if jess.mp > LIST_OF_SKILL_POINTS[7]:
                glimmer_button['state'] = NORMAL
            if jess.mp > LIST_OF_SKILL_POINTS[8]:
                illuminate_button['state'] = NORMAL

    def disable_buttons(user):
        """Disables Buttons"""
        attack_button['state'] = DISABLED
        defend_button['state'] = DISABLED
        if user == isla:
            heal_button['state'] = DISABLED
            aura_button['state'] = DISABLED
            trick_button['state'] = DISABLED
        elif user == rosa:
            boulder_brute_button['state'] = DISABLED
            carbon_protect_button['state'] = DISABLED
            pressurise_button['state'] = DISABLED
        else:
            prismatic_beam_button['state'] = DISABLED
            glimmer_button['state'] = DISABLED
            illuminate_button['state'] = DISABLED

    def inflict_damage(character):
        """Net Attack is inflicted onto the Character."""
        global net_attack
        character.hp -= int(net_attack)
        net_attack = 0

    def check_health():
        """Cleans Health."""
        global user_player, user_player2, comp_enemy, comp_enemy2
        if comp_enemy.hp < 0:
            comp_enemy.hp = 0
        if user_player.hp < 0:
            user_player.hp = 0
        if user_player.hp > user_player.HP:
            user_player.hp = user_player.HP
        if number_of_enemies.get() == 2:
            if comp_enemy2.hp < 0:
                comp_enemy2.hp = 0
            if user_player2.hp < 0:
                user_player2.hp = 0
            if user_player2.hp > user_player2.HP:
                user_player2.hp = user_player2.HP
        screen1.update()

    def check_vital_signs(enemy, player):
        """Checks if Enemy/Player is alive. If true, they make their move against each other."""
        if enemy.hp <= 0 or player.hp <= 0:
            return False
        else:
            return True

    def enemy_move(enemy, player):
        """The Enemy will decide whether to Attack/Defend."""
        global enemy_defense, enemy2_defense
        alive = check_vital_signs(enemy, player)
        if alive:
            pass
        else:
            return
        computer_is_deciding = True
        while computer_is_deciding:
            choices = ["attack", "defend"]
            comp_choice = random.choice(choices)
            if comp_choice == "attack":
                attack(enemy, player)
                computer_is_deciding = False
            else:
                if enemy == comp_enemy:
                    if enemy_defense < 4:
                        enemy_defense += 1
                        defend(enemy)
                        computer_is_deciding = False
                    else:
                        continue
                elif enemy == comp_enemy2:
                    if enemy2_defense < 4:
                        enemy2_defense += 1
                        defend(enemy)
                        computer_is_deciding = False
                    else:
                        continue
        screen1.update()

    def player_move(enemy, player):
        """The Player will decide whether to Attack/Defend/Skill."""
        global choosing_action, battling, player_defense, next_move, content
        alive = check_vital_signs(enemy, player)
        if alive:
            pass
        else:
            return
        choosing_action = True
        while choosing_action:
            enable_buttons(player)

            def player_move_clicked(button):
                """Assigns Commands to Buttons. Includes Additional Functions"""
                global choosing_action
                if button == attack_button:
                    attack(player, enemy)
                elif button == defend_button:
                    defend(player)
                elif button == heal_button:
                    isla.heal(content)
                elif button == aura_button:
                    isla.aura(enemy, content)
                elif button == trick_button:
                    isla.trick(enemy, content)
                elif button == boulder_brute_button:
                    rosa.boulder_brute(enemy, content)
                elif button == carbon_protect_button:
                    rosa.carbon_protect(content)
                elif button == pressurise_button:
                    rosa.pressurise(content)
                elif button == prismatic_beam_button:
                    jess.prismatic_beam(enemy, content)
                elif button == glimmer_button:
                    jess.glimmer(content)
                elif button == illuminate_button:
                    jess.illuminate(enemy, content)
                display_player_stats()
                display_enemy_stats()
                disable_buttons(player)
                choosing_action = False

            attack_button.config(command=lambda: player_move_clicked(attack_button))
            defend_button.config(command=lambda: player_move_clicked(defend_button))
            heal_button.config(command=lambda: player_move_clicked(heal_button))
            aura_button.config(command=lambda: player_move_clicked(aura_button))
            trick_button.config(command=lambda: player_move_clicked(trick_button))
            boulder_brute_button.config(command=lambda: player_move_clicked(boulder_brute_button))
            carbon_protect_button.config(command=lambda: player_move_clicked(carbon_protect_button))
            pressurise_button.config(command=lambda: player_move_clicked(pressurise_button))
            prismatic_beam_button.config(command=lambda: player_move_clicked(prismatic_beam_button))
            glimmer_button.config(command=lambda: player_move_clicked(glimmer_button))
            illuminate_button.config(command=lambda: player_move_clicked(illuminate_button))

            screen1.update()

    def generating_an_enemy(numb):
        """Generates Enemies"""
        global LIST_OF_CHARACTERS, comp_enemy_choice, content
        insert_text("\n\nGenerating an enemy...", content)
        generating = True
        while generating:
            enemy_name = random.choice(LIST_OF_CHARACTERS[3:])
            if numb == 1:
                comp_enemy_choice = enemy_name.name
            else:
                if enemy_name.name == comp_enemy_choice:
                    continue
            insert_text(f"\nYour enemy will be {enemy_name.name}!", content)
            return enemy_name

    def start_game_logic():
        """Spawns Enemies. StartsGame."""
        global user_player, user_player2, comp_enemy, comp_enemy2, number_of_enemies, next_move, content
        if number_of_enemies.get() == 1:
            comp_enemy = generating_an_enemy(1)
            display_enemy_stats()
            display_enemy_char()
            insert_text("\n\nLet the battle begin! Good Luck.", content)
            if user_player.SP >= comp_enemy.SP:
                insert_text(f"\n{user_player.name} moves first.", content)
                battle(user_player)
            else:
                insert_text(f"\n{comp_enemy.name} moves first.", content)
                battle(comp_enemy)
            return
        else:
            next_move = True
            insert_text("\n\nFor your first enemy...", content)
            comp_enemy = generating_an_enemy(1)
            insert_text("\n\nFor your second enemy...", content)
            comp_enemy2 = generating_an_enemy(2)
            display_enemy_stats()
            display_enemy_char()
            insert_text("\n\nLet the battle begin! Good Luck.", content)
            if user_player.SP + user_player2.SP >= comp_enemy.SP + comp_enemy2.SP:
                insert_text(f"\n{user_player.name} and {user_player2.name} move first.", content)
                battle(user_player)
            else:
                insert_text(f"\n{comp_enemy.name} and {comp_enemy2.name} move first.", content)
                battle(comp_enemy)
            return

    def continue_game():
        """Returns True if the game will continue."""
        global user_player, user_player2, comp_enemy, comp_enemy2, number_of_enemies, turns, rounds, content
        check_health()
        if number_of_enemies.get() == 1:
            if user_player.hp <= 0:
                insert_text(f"\nYour Enemy, {comp_enemy.name},  has won!", content)
                insert_text("\nTry your luck next time.", content)
                return False
            if comp_enemy.hp <= 0:
                insert_text(f"\nYour Player, {user_player.name}, has won!", content)
                insert_text("\nCongratulations!", content)
                return False
        if number_of_enemies.get() == 2:
            if user_player.hp <= 0 and user_player2.hp <= 0:
                insert_text(f"\nYour Enemies, {comp_enemy.name} and {comp_enemy2.name}, have won!", content)
                insert_text("\nTry your luck next time.", content)
                return False
            if comp_enemy.hp <= 0 and comp_enemy2.hp <= 0:
                insert_text(f"\nYour Players, {user_player.name} and {user_player2.name}, have won!", content)
                insert_text("\nCongratulations!", content)
                return False
            if comp_enemy.hp <= 0 and user_player2.hp <= 0:
                number_of_enemies.set(1)
                comp_enemy = comp_enemy2
                insert_text("\nThe last two remaining characters will now battle! They are adjusting their positions \
during this round.", content)
                turns = 2
                rounds += 1
                if user_player.SP >= comp_enemy.SP:
                    battle(user_player)
                else:
                    battle(comp_enemy)
                return False
            if user_player.hp <= 0 and comp_enemy2.hp <= 0:
                number_of_enemies.set(1)
                user_player = user_player2
                insert_text("\nThe last two remaining characters will now battle! They are adjusting their positions \
during this round.", content)
                turns = 2
                rounds += 1
                if user_player.SP >= comp_enemy.SP:
                    battle(user_player)
                else:
                    battle(comp_enemy)
                return False
        return True

    def battle(faster_player):
        """Player and Enemy are battling each other. The Faster Player goes on Even turns."""
        global user_player, user_player2, comp_enemy, comp_enemy2, turns, rounds, battling, next_move, content
        if faster_player == user_player:
            user = 0
        else:
            user = 1
        battling = True
        while battling:
            insert_text(f"\n\n----------Round {rounds}----------", content)
            check_health()
            if continue_game():
                pass
            else:
                break
            if turns % 2 == 0:
                # Faster Player goes on Even Turn
                if user == 0:
                    # Player is faster
                    player_move(comp_enemy, user_player)
                    inflict_damage(comp_enemy)
                    display_player_stats()
                    display_enemy_stats()
                    if next_move:
                        player_move(comp_enemy2, user_player2)
                        inflict_damage(comp_enemy2)
                        display_player_stats()
                        display_enemy_stats()
                else:
                    # Enemy is faster
                    enemy_move(comp_enemy, user_player)
                    inflict_damage(user_player)
                    display_player_stats()
                    display_enemy_stats()
                    if next_move:
                        enemy_move(comp_enemy2, user_player2)
                        inflict_damage(user_player2)
                        display_player_stats()
                        display_enemy_stats()
            else:
                # Slower Player goes on Odd Turn
                if user == 0:
                    # Enemy is slower
                    enemy_move(comp_enemy, user_player)
                    inflict_damage(user_player)
                    display_player_stats()
                    display_enemy_stats()
                    if next_move:
                        enemy_move(comp_enemy2, user_player2)
                        inflict_damage(user_player2)
                        display_player_stats()
                        display_enemy_stats()
                else:
                    # Player is faster
                    player_move(comp_enemy, user_player)
                    inflict_damage(comp_enemy)
                    display_player_stats()
                    display_enemy_stats()
                    if next_move:
                        player_move(comp_enemy2, user_player2)
                        inflict_damage(comp_enemy2)
                        display_player_stats()
                        display_enemy_stats()
            turns += 1
            rounds += 1

    def display_player_stats():
        """Displays Player Stats"""
        global number_of_enemies, stats, stats2
        if number_of_enemies.get() == 1:
            stats.set(user_player.display_stats())
            stat = Label(health_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats, justify=LEFT)
            stat.grid(row=0, column=0)
        if number_of_enemies.get() == 2:
            stats.set(user_player.display_stats())
            stat = Label(health_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats, justify=LEFT)
            stat.grid(row=0, column=0)
            stats2.set(user_player2.display_stats())
            stat2 = Label(health_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats2)
            stat2.config(justify=LEFT)
            stat2.grid(row=1, column=0)

    def display_enemy_stats():
        """Displays Enemy Stats"""
        global number_of_enemies, stats3, stats4
        if number_of_enemies.get() == 1:
            stats3.set(comp_enemy.display_stats())
            stat3 = Label(health_section2, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats3)
            stat3.config(justify=LEFT)
            stat3.grid(row=0, column=0)
        if number_of_enemies.get() == 2:
            stats3.set(comp_enemy.display_stats())
            stat3 = Label(health_section2, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats3)
            stat3.config(justify=LEFT)
            stat3.grid(row=0, column=0)
            stats4.set(comp_enemy2.display_stats())
            stat4 = Label(health_section2, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, textvariable=stats4)
            stat4.config(justify=LEFT)
            stat4.grid(row=1, column=0)

    # --NAVIGATION BUTTONS SECTION--
    if number_of_enemies.get() == 1:
        mode_title = Label(screen6_frame, text="-----1 V 1-----", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
        mode_title.grid(row=0, column=0, sticky="w")
    if number_of_enemies.get() == 2:
        mode_title = Label(screen6_frame, text="-----2 V 2-----", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
        mode_title.grid(row=0, column=0, sticky="w")
    exit_ = Button(screen6_frame, text="Exit", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, command=exit_battle)
    exit_.grid(row=0, column=1, sticky="e")
    restart = Button(screen6_frame, text="Restart", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, command=restart_battle)
    restart.grid(row=0, column=1, sticky="e", padx=70)
    main_frame = Frame(screen6_frame, height=600, width=1200, bg=BG_COLOUR)
    main_frame.grid_propagate(False)
    main_frame.grid(row=1, column=0, columnspan=2)

    # --CHARACTER DISPLAY SECTION--
    image_frame = Frame(main_frame, height=350, width=800, bg=BG_COLOUR)
    image_frame.grid(column=0, row=0)
    image_frame.grid_propagate(False)
    image_frame.rowconfigure(0, weight=1)
    for numb in range(0, 5):
        image_frame.columnconfigure(numb, weight=1)
    Label(image_frame, bg=BG_COLOUR, image=mod_photo8).grid(row=0, column=2)

    # --ACTION BUTTONS SECTION--
    buttons_frame = Frame(main_frame, height=250, width=800, bg=BG_COLOUR)
    buttons_frame.grid(column=0, row=1)
    buttons_frame.pack_propagate(False)
    buttons_frame.rowconfigure(0, weight=1)
    buttons_section = LabelFrame(buttons_frame, height=240, width=380, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT)
    buttons_section.config(text="What would you like to do with your player?")
    buttons_section.grid(row=0, column=1)
    buttons_section.pack_propagate(False)
    attack_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Attack", width=35)
    attack_button.pack(expand=True)
    defend_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Defend", width=35)
    defend_button.pack(expand=True)
    heal_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Heal(50MP)", width=35)
    aura_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Aura(50MP)", width=35)
    trick_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Trick(90MP)", width=35)
    boulder_brute_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, width=35)
    boulder_brute_button.config(text="Boulder Brute(75MP)")
    carbon_protect_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, width=35)
    carbon_protect_button.config(text="Carbon Protect(80MP)")
    pressurise_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, width=35)
    pressurise_button.config(text="Pressurise(50MP)")
    prismatic_beam_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, width=35)
    prismatic_beam_button.config(text="Prismatic Beam(80MP)")
    glimmer_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Glimmer(50MP)")
    glimmer_button.config(width=35)
    illuminate_button = Button(buttons_section, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, text="Illuminate(25MP)")
    illuminate_button.config(width=35)

    # --PLAYER STATS SECTION--
    health_section = LabelFrame(buttons_frame, height=240, width=200, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT)
    health_section.config(text="Player Stats")
    health_section.grid_propagate(False)
    health_section.grid(row=0, column=0)
    health_section.columnconfigure(0, weight=1)
    for num in range(0, 2):
        health_section.rowconfigure(num, weight=1)

    # --ENEMY STATS SECTION--
    health_section2 = LabelFrame(buttons_frame, height=240, width=200, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT)
    health_section2.config(text="Enemy Stats")
    health_section2.grid_propagate(False)
    health_section2.grid(row=0, column=2)
    health_section2.columnconfigure(0, weight=1)
    for num in range(0, 2):
        health_section2.rowconfigure(num, weight=1)

    # -- MESSAGE LOG SECTION--
    content_frame = Frame(main_frame, height=600, width=400, bg=BG_COLOUR)
    content_frame.pack_propagate(False)
    content_frame.grid(column=1, row=0, rowspan=2)
    content_frame.rowconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)
    content = Text(content_frame, height=60, width=54, fg=BG_COLOUR, bg=FG_COLOUR)
    content.config(wrap='word', state=DISABLED)
    content.pack(side=LEFT)
    scroll_bar = Scrollbar(content_frame, orient=VERTICAL, command=content.yview)
    scroll_bar.pack(side=RIGHT, fill='y')
    content.config(yscrollcommand=scroll_bar.set)

    # --CARRIES OUT STEPS BEFORE GAME STARTS--
    disable_buttons(user_player)
    display_player_stats()
    display_player_char()
    start_game_logic()

def start_game():
    """Displays Preparing Game Screen"""
    global screen5_frame
    screen5_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
    for num in range(0, 2):
        screen5_frame.grid_columnconfigure(num, weight=1)
    screen5_frame.grid(row=0, column=0)
    screen5_frame.grid_propagate(False)
    title = Label(screen5_frame, text="Preparing Game...", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    title.grid(row=0, column=0, sticky="w")
    back_ = Button(screen5_frame, text="Back", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    back_.config(command=lambda: back(screen5_frame))
    back_.grid(row=0, column=1, sticky="e")
    main_frame = Frame(screen5_frame, height=560, width=1200, bg=BG_COLOUR, padx=50)
    main_frame.grid_propagate(False)
    main_frame.grid(row=1, column=0, columnspan=2)
    next_ = Button(screen5_frame, text="Next", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, command=battle_screen)
    next_['state'] = DISABLED
    next_.grid(row=2, column=1, sticky="e")

    def char_buttons_1v1():
        """Configures 1VS1 Buttons"""
        def clicked(button):
            """Disables/Enables Necessary Buttons"""
            global user_player
            button.config(fg=BG_COLOUR, bg=FG_COLOUR)
            for butt in button_list:
                if butt != button:
                    butt['state'] = DISABLED
                    next_['state'] = NORMAL
                else:
                    if butt == char1:
                        user_player = isla
                    elif butt == char2:
                        user_player = rosa
                    else:
                        user_player = jess
        char1 = Button(main_frame, image=mod_photo2, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char1), width=240)
        char1.config(text=f"{isla.display_stats()}\r--Skills--\rHeal\rAura\rTrick")
        char1.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char1.grid(row=3, column=0, sticky="w")
        char2 = Button(main_frame, image=mod_photo3, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char2), width=240)
        char2.config(text=f"{rosa.display_stats()}\r--Skills--\rBoulder Brute\rCarbon Protect\rPressurise")
        char2.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char2.grid(row=3, column=1, sticky="w")
        char3 = Button(main_frame, image=mod_photo4, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char3), width=240)
        char3.config(text=f"{jess.display_stats()}\r--Skills--\rPrismatic Beam\rGlimmer\rIlluminate")
        char3.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char3.grid(row=3, column=2, sticky="w")
        button_list = [char1, char2, char3]

    def char_buttons_2v2():
        """Configures 2VS2 Buttons"""
        def clicked(button):
            """Disables/Enables Necessary Buttons"""
            global user_player, user_player2, clicked_buttons
            clicked_buttons.append(button)
            button.config(fg=BG_COLOUR, bg=FG_COLOUR)
            if len(clicked_buttons) == 2:
                for butt in button_list:
                    if butt not in clicked_buttons:
                        butt['state'] = DISABLED
                        next_['state'] = NORMAL
                    elif clicked_buttons.index(butt) == 0:
                        if butt == char1:
                            user_player = isla
                        elif butt == char2:
                            user_player = rosa
                        else:
                            user_player = jess
                    elif clicked_buttons.index(butt) == 1:
                        if butt == char1:
                            user_player2 = isla
                        elif butt == char2:
                            user_player2 = rosa
                        else:
                            user_player2 = jess
        char1 = Button(main_frame, image=mod_photo2, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char1), width=240)
        char1.config(text=f"{isla.display_stats()}\r--Skills--\rHeal\rAura\rTrick")
        char1.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char1.grid(row=3, column=0, sticky="w")
        char2 = Button(main_frame, image=mod_photo3, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char2), width=240)
        char2.config(text=f"{rosa.display_stats()}\r--Skills--\rBoulder Brute\rCarbon Protect\rPressurise")
        char2.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char2.grid(row=3, column=1, sticky="w")
        char3 = Button(main_frame, image=mod_photo4, bg=BG_COLOUR, fg=FG_COLOUR, command=lambda: clicked(char3), width=240)
        char3.config(text=f"{jess.display_stats()}\r--Skills--\rPrismatic Beam\rGlimmer\rIlluminate")
        char3.config(font=SMALL_FONT, compound=TOP, justify=LEFT)
        char3.grid(row=3, column=2, sticky="w")
        button_list = [char1, char2, char3]

    def restart_button_states():
        """Restarts Game Mode Buttons"""
        global clicked_buttons
        option1.config(fg=FG_COLOUR, bg=BG_COLOUR)
        option2.config(fg=FG_COLOUR, bg=BG_COLOUR)
        clicked_buttons = []

    def option1_func():
        """Displays 1VS1 Options"""
        number_of_enemies.set(1)
        restart_button_states()
        option1.config(bg=FG_COLOUR, fg=BG_COLOUR)
        q2 = Label(main_frame, text="Choose ONE character:", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
        q2.grid(row=2, column=0, sticky="w")
        char_buttons_1v1()

    def option2_func():
        """Displays 2VS2 Options"""
        number_of_enemies.set(2)
        restart_button_states()
        option2.config(bg=FG_COLOUR, fg=BG_COLOUR)
        q2 = Label(main_frame, text="Choose TWO characters:", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
        q2.grid(row=2, column=0, sticky="w")
        char_buttons_2v2()

    # --GAME MODE OPTIONS--
    q1 = Label(main_frame, text="Choose a game mode:", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    q1.grid(row=0, column=0, sticky="w")
    option1 = Button(main_frame, text="1 VS 1", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, height=4, width=25)
    option1.config(command=option1_func)
    option1.grid(row=1, column=0)
    option2 = Button(main_frame, text="2 VS 2", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, height=4, width=25)
    option2.config(command=option2_func)
    option2.grid(row=1, column=1)

def view_players():
    """Displays View Players Screen"""
    screen4_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
    for num in range(0, 2):
        screen4_frame.grid_columnconfigure(num, weight=1)
    screen4_frame.grid(row=0, column=0)
    screen4_frame.grid_propagate(False)
    title = Label(screen4_frame, text="Players", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    title.grid(row=0, column=0, sticky="w")
    back_ = Button(screen4_frame, text="Back", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    back_.config(command=lambda: back(screen4_frame))
    back_.grid(row=0, column=1, sticky="e")
    main_frame = Frame(screen4_frame, height=600, width=1200, bg=BG_COLOUR)
    main_frame.grid(row=1, column=0, columnspan=2)
    Label(main_frame, width=250, height=200, image=mod_photo2, bg=BG_COLOUR).grid(row=0, column=0)
    Label(main_frame, width=250, height=200, image=mod_photo3, bg=BG_COLOUR).grid(row=1, column=0)
    Label(main_frame, width=250, height=200, image=mod_photo4, bg=BG_COLOUR).grid(row=2, column=0)
    isla_stats = LabelFrame(main_frame, text="Isla", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, width=900, height=190)
    isla_stats.grid_propagate(False)
    isla_stats.grid(row=0, column=1)
    rosa_stats = LabelFrame(main_frame, text="Rosa", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, width=900, height=190)
    rosa_stats.grid_propagate(False)
    rosa_stats.grid(row=1, column=1)
    jess_stats = LabelFrame(main_frame, text="Jess", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR, width=900, height=190)
    jess_stats.grid_propagate(False)
    jess_stats.grid(row=2, column=1)
    for num in range(0, 2):
        isla_stats.rowconfigure(num, weight=1)
        rosa_stats.rowconfigure(num, weight=1)
        jess_stats.rowconfigure(num, weight=1)
    isla_num = Label(isla_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    isla_num.config(text=f"{isla.display_stats()}")
    isla_num.grid(row=0, column=0, sticky="w")
    isla_skill = Label(isla_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    isla_skill.config(text='''
SKILLS: Heal - 50P - Increases your current HP by 50%.
                 Aura - 50P - Permanently lowers the enemy's DP by 50%.
                 Trick - 90P - Acts as a force-field for all players. Lasts one round. The enemy's AP is inflicted onto\
 themselves, their turn is skipped.
    ''')
    isla_skill.grid(row=1, column=0, sticky="w")
    rosa_num = Label(rosa_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    rosa_num.config(text=f"{rosa.display_stats()}")
    rosa_num.grid(row=0, column=0, sticky="w")
    rosa_skill = Label(rosa_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    rosa_skill.config(text='''
SKILLS: Boulder Brute - 75P - Combines the AP of both characters, inflicting 75% of that value onto the enemy. 
                 Carbon Protect - 80P - All players will be immune to any damage. Lasts one round. Enemy's turn is\
 skipped.
                 Pressurise - 50P - Permanently increases your DP by 15%.
''')
    rosa_skill.grid(row=1, column=0, sticky="w")
    jess_num = Label(jess_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    jess_num.config(text=f"{jess.display_stats()}")
    jess_num.grid(row=0, column=0, sticky="w")
    jess_skill = Label(jess_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    jess_skill.config(text='''
SKILLS: Prismatic Beam - 80P - Net Damage inflicted is 2x the Enemy's DP.
                 Glimmer - 50P - Permanently increases your AP by 50%.
                 Illuminate - 25P - Absorbs 10% of the Ene,y's DP.
''')
    jess_skill.grid(row=1, column=0, sticky="w")

def view_enemies():
    """Displays View Enemies Screen"""
    screen3_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
    for num in range(0, 2):
        screen3_frame.grid_columnconfigure(num, weight=1)
    screen3_frame.grid(row=0, column=0)
    screen3_frame.grid_propagate(False)
    title = Label(screen3_frame, text="Enemies", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    title.grid(row=0, column=0, sticky="w")
    back_ = Button(screen3_frame, text="Back", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    back_.config(command=lambda:back(screen3_frame))
    back_.grid(row=0, column=1, sticky="e")
    main_frame = Frame(screen3_frame, height=600, width=1200, bg=BG_COLOUR)
    main_frame.grid(row=1, column=0, columnspan=2)
    Label(main_frame, width=250, height=200, image=mod_photo5, bg=BG_COLOUR).grid(row=0, column=0)
    Label(main_frame, width=250, height=200, image=mod_photo6, bg=BG_COLOUR).grid(row=1, column=0)
    Label(main_frame, width=250, height=200, image=mod_photo7, bg=BG_COLOUR).grid(row=2, column=0)
    violet_stats = LabelFrame(main_frame, text="Violet", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    violet_stats.config(width=900, height=190)
    violet_stats.grid_propagate(False)
    violet_stats.grid(row=0, column=1)
    merida_stats = LabelFrame(main_frame, text="Merida", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    merida_stats.config(width=900, height=190)
    merida_stats.grid_propagate(False)
    merida_stats.grid(row=1, column=1)
    diego_stats = LabelFrame(main_frame, text="Diego", font=NORM_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    diego_stats.config(width=900, height=190)
    diego_stats.grid_propagate(False)
    diego_stats.grid(row=2, column=1)
    for num in range(0, 2):
        violet_stats.rowconfigure(num, weight=1)
        merida_stats.rowconfigure(num, weight=1)
        diego_stats.rowconfigure(num, weight=1)
    violet_num = Label(violet_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    violet_num.config(text=f"{violet.display_stats()}")
    violet_num.grid(row=0, column=0, sticky="w")
    violet_skill = Label(violet_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    violet_skill.config(text="Enemies have no magic skills.")
    violet_skill.grid(row=1, column=0, sticky="w")
    merida_num = Label(merida_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    merida_num.config(text=f"{merida.display_stats()}")
    merida_num.grid(row=0, column=0, sticky="w")
    merida_skill = Label(merida_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    merida_skill.config(text="Enemies have no magic skills.")
    merida_skill.grid(row=1, column=0, sticky="w")
    diego_num = Label(diego_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    diego_num.config(text=f"{diego.display_stats()}")
    diego_num.grid(row=0, column=0, sticky="w")
    diego_skill = Label(diego_stats, bg=BG_COLOUR, fg=FG_COLOUR, font=SMALL_FONT, justify=LEFT)
    diego_skill.config(text="Enemies have no magic skills.")
    diego_skill.grid(row=1, column=0, sticky="w")

def game_settings():
    """Displays Game Settings Screen"""
    screen2_frame = Frame(screen1, width=1200, height=658, bg=BG_COLOUR)
    for num in range(0, 2):
        screen2_frame.grid_columnconfigure(num, weight=1)
    screen2_frame.grid(row=0, column=0)
    title = Label(screen2_frame, text="Game Settings", font=BIG_FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    title.grid(row=0, column=0, sticky="w")
    back_ = Button(screen2_frame, text="Back", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT)
    back_.config(command=lambda: back(screen2_frame))
    back_.grid(row=0, column=1, sticky="e")
    frame = Frame(screen2_frame, height=600, width=1200, bg=BG_COLOUR)
    frame.grid(row=1, column=0, columnspan=2)
    frame.grid_propagate(False)
    for num in range(5):
        frame.columnconfigure(num, weight=1)
        frame.rowconfigure(num, weight=1)
    Label(frame, text="Audio", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT).grid(row=0, column=0)
    Label(frame, text="Language", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT).grid(row=1, column=0)
    Label(frame, text="Difficulty", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT).grid(row=2, column=0)
    Radiobutton(frame, text="On", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT).grid(row=0, column=1)
    Radiobutton(frame, text="Off", fg=FG_COLOUR, bg=BG_COLOUR, font=NORM_FONT).grid(row=0, column=2)
    var = StringVar()
    language_options = OptionMenu(frame, var, *LIST_OF_LANGUAGES)
    language_options.config(width=15, bg=BG_COLOUR, fg=FG_COLOUR, font=NORM_FONT)
    language_options.grid(row=1, column=1)
    difficulty_options = Scale(frame, orient=HORIZONTAL, bg=BG_COLOUR, fg=FG_COLOUR, font=NORM_FONT, width=30)
    difficulty_options.config(from_=1, to=5)
    difficulty_options.grid(row=2, column=1)

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

# ----------SCREEN 1 WIDGETS----------
Label(
    screen1_frame,
    text="*✧･ﾟ:*Alchemy Saga*:ﾟ･✧*",
    font=BIG_FONT,
    fg=FG_COLOUR,
    bg=BG_COLOUR
).grid(row=0, column=0, columnspan=2)

# --FRAMES--
left_home_frame = Frame(screen1_frame, height=600, width=300)
left_home_frame.config(bg=BG_COLOUR, highlightthickness=1, highlightcolor=FG_COLOUR, pady=5, padx=5)
left_home_frame.grid(row=1, column=0)
left_home_frame.pack_propagate(False)
right_home_frame = Frame(screen1_frame, height=600, width=900)
right_home_frame.grid(row=1, column=1)
right_home_frame.grid_propagate(False)

# --PHOTOS--
Label(right_home_frame, image=mod_photo1).place(x=1, y=1)

# --BUTTONS--
button1 = Button(left_home_frame, text="View Players", fg=FG_COLOUR, bg=BG_COLOUR, width=30, height=3, font=NORM_FONT)
button1.config(command=view_players)
button1.pack(expand=True)
button2 = Button(left_home_frame, text="View Enemies", fg=FG_COLOUR, bg=BG_COLOUR, width=30, height=3, font=NORM_FONT)
button2.config(command=view_enemies)
button2.pack(expand=True)
button3 = Button(left_home_frame, text="Game Settings", fg=FG_COLOUR, bg=BG_COLOUR, width=30, height=3, font=NORM_FONT)
button3.config(command=game_settings)
button3.pack(expand=True)
button4 = Button(left_home_frame, text="Exit", fg=FG_COLOUR, bg=BG_COLOUR, width=30, height=3, font=NORM_FONT)
button4.config(command=lambda: back(screen1))
button4.pack(expand=True)
button5 = Button(right_home_frame, text="Start Game", fg=FG_COLOUR, bg=BG_COLOUR, width=30, height=3, font=NORM_FONT)
button5.config(command=start_game)
button5.place(relx=0.5, rely=0.7)

# --------------------START--------------------
screen1.mainloop()