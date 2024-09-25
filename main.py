import os
from random import randint
import readchar as readchar

# Constants
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11

# Variables
my_position = [17, 3]
direction = None
start_combat = None
end_game = False
map_enemies = [[13, 4], [11, 7], [5, 11], [12, 14]]
enemy_pokemons_index = [0, 1, 2, 3, 4]
enemy_position = 0

obstacle_definition = """\
#######             
#######             
#######             
#######             
#######             
#######     ########
#######     ########
            ########
            ########
            ########
            ########
            ########
#######             
#######             
#######             
#######     ########
#######     ########
#######     ########
#######     ########
#######     ########\
"""

pikachu = """\
                     /\ 
         ___________/-| 
         \_|_         | 
           /   · , ·  | 
  ____     \  o  U  o | 
 |__  |    /  D       \D
     \__\ |            |
         L=\__________/ 
             V      V   
                        \
"""

squirtel = """\
      _________         
     / V    V  \        
    |    U      |       
 ____\_________/        
/____/________//\ ____  
     |  |  /  /| \|   \ 
     |>-+-/__/ \ \|  \ |
     /\_/\___\/ / ___/  
    /   /   \   |       
    |___|   |___|       \
"""

bulbasaur = """\


     /\______/\ M M    
    /  O .. O  \  \ \  
    \  L____|  |  / /  
     |         ·     \ 
     |  |___/ · /__/· |
     \ ·|  /·  /   \  /
      ---  ----     -- 
                       \
"""

charmander = """\

       ________        
     /         \       
    |  O   O    |      
    (__  V     /       
  ____/ /--\   |____/\ 
  \__/ /    \  ____/\/ 
    /\|_____/  \----/\ 
    \  /    \   |----/ 
    ---      ----      \
"""

zubat = """\

        /\___/\        
    /\  | 6 6 |  /\    
   /  \ \ <"> / /  \   
  / ,__`~)---(~___, \  
 /.'    /___/      '.\ 
        \___\          
         \__\          
         /  /          
         \W\           \
"""

# create Pokémon images

pokemon_list = []

pokemon_definition = [list(row) for row in pikachu.split("\n")]
pokemon_list.append(pokemon_definition)

pokemon_definition = [list(row) for row in squirtel.split("\n")]
pokemon_list.append(pokemon_definition)

pokemon_definition = [list(row) for row in bulbasaur.split("\n")]
pokemon_list.append(pokemon_definition)

pokemon_definition = [list(row) for row in charmander.split("\n")]
pokemon_list.append(pokemon_definition)

pokemon_definition = [list(row) for row in zubat.split("\n")]
pokemon_list.append(pokemon_definition)

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while direction != "q" and end_game == False:

    # Map drawing

    start_combat = False
    enemy_position = 0

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "   "
            object_in_cell = None
            tail_in_cell = None

            for enemy in map_enemies:
                if enemy[POS_X] == coordinate_x and enemy[POS_Y] == coordinate_y:
                    char_to_draw = " R "
                    object_in_cell = enemy
                    if not start_combat:
                        enemy_position += 1

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @ "

                if object_in_cell:
                    map_enemies.remove(object_in_cell)
                    start_combat = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "###"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Character moving

    direction = readchar.readchar()
    new_position = None

    if direction == "Q":
        break

    if direction == "w" and (my_position[POS_Y]) % MAP_HEIGHT != 0:
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1)]

    elif direction == "s" and (my_position[POS_Y] + 1) % MAP_HEIGHT != 0:
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1)]

    elif direction == "a" and (my_position[POS_X]) % MAP_WIDTH != 0:
        new_position = [(my_position[POS_X] - 1), my_position[POS_Y]]

    elif direction == "d" and (my_position[POS_X] + 1) % MAP_WIDTH != 0:
        new_position = [(my_position[POS_X] + 1), my_position[POS_Y]]

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

    # Pokemon combat

    # Rival stats

    rival_stats = []

    if enemy_pokemons_index[enemy_position] == 1:
        rival_stats.append("Squirtel")
        rival_stats.append("Water pistol")
        rival_stats.append(80)
    elif enemy_pokemons_index[enemy_position] == 2:
        rival_stats.append("Bulbasaur")
        rival_stats.append("Leaf strom")
        rival_stats.append(70)
    elif enemy_pokemons_index[enemy_position] == 3:
        rival_stats.append("Charmander")
        rival_stats.append("Flamethrower")
        rival_stats.append(75)
    elif enemy_pokemons_index[enemy_position] == 4:
        rival_stats.append("Zubat")
        rival_stats.append("Tornado")
        rival_stats.append(90)

    # Other variables

    LIFE_BAR_WIDTH = 10
    my_total_lives = 90
    my_current_lives = my_total_lives

    rival_total_lives = rival_stats[2]
    rival_current_lives = rival_total_lives

    if start_combat:
        print("--------------------------------")
        print("--------------------------------")
        print("       Red vs Team Rocket       ")
        print("--------------------------------")
        print("--------------------------------")

        input("Press enter to start...")

        os.system("cls")

        # Print pokemons

        while my_current_lives > 0 and rival_current_lives > 0:

            for y in range(10):

                print("|", end="")

                for x in range(48):

                    char_to_draw = ""

                    if x < 24:
                        for char in pokemon_list[0][y][x]:
                            char_to_draw = char
                    elif x == 24:
                        char_to_draw = " " * 10
                    else:
                        for char in pokemon_list[enemy_position][y][(x - 1) % 24]:
                            char_to_draw = char

                    print("{}".format(char_to_draw), end="")
                print("|")

            # Print lives bars
            my_life = int(my_current_lives / my_total_lives * LIFE_BAR_WIDTH)
            rival_life = int(rival_current_lives / rival_total_lives * LIFE_BAR_WIDTH)
            print("{} [{}{}] {}".format("Pikachu", "#" * int(my_life), " " * int(LIFE_BAR_WIDTH - my_life),
                                        my_current_lives) + (" " * 10) +
                  "{} [{}{}] {}".format(rival_stats[0], "#" * int(rival_life), " " * int(LIFE_BAR_WIDTH - rival_life),
                                        rival_current_lives))

            # Pokemon combat

            print("\nRivals turn")
            rival_attack = randint(1, 2)

            if rival_attack == 1:
                print("{} attack with Tackle".format(rival_stats[0]))
                my_current_lives -= 10
            else:
                print("{} attack with {}".format(rival_stats[0], rival_stats[1]))
                my_current_lives -= 11

            if my_current_lives < 0:
                my_current_lives = 0

            # Life Bars

            print("\nYour turn")

            print("A- Tackle\n"
                  "B- Ray\n"
                  "C- Thunder\n"
                  "D- Iron tail\n"
                  "N- Not attack\n")

            my_attack = None
            while my_attack not in ["A", "B", "C", "D", "N"]:
                my_attack = input("What do you want to do? ")

            if my_attack == "A":
                print("Pikachu attack with Tackle")
                rival_current_lives -= 1
            elif my_attack == "B":
                print("SPikachu attack with Ray")
                rival_current_lives -= 12
            elif my_attack == "C":
                print("Pikachu attack with Thunder")
                rival_current_lives -= 9
            elif my_attack == "D":
                print("Pikachu attack with Iron tail")
                rival_current_lives -= 15

            if rival_current_lives < 0:
                rival_current_lives = 0

            # barras de vida

            input("Press enter to continue...\n\n")

            os.system("cls")

        if rival_current_lives > my_current_lives:
            print("The rival won!")
            end_game = True
        else:
            print("You won!")
            pokemon_list.remove(pokemon_list[enemy_position])
            enemy_pokemons_index.pop(enemy_position)

        input("Press enter to continue...")

        if len(map_enemies) == 0:
            end_game = True

        os.system("cls")

print("Congratulations!!\n"
      "You won!!!")