import random

from Monty_Hall_Analysis import print_values

result_list = []
iteration = 5000

for guess in range(iteration):
    doors = ['a', 'b', 'c']
    player_choice = random.choice(doors)
    prize_door = random.choice(doors)
    trial = [player_choice]

    opens = player_choice
    while opens == player_choice or opens == prize_door:
        opens = random.choice(doors)

    doors.remove(opens)
    doors.remove(player_choice)

    player_choice = random.choice(doors)

    trial.append(player_choice)

    if player_choice == prize_door:
        trial.append(1)
    else:
        trial.append(0)

    result_list.append(trial)

print_values(result_list)
