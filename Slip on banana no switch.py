import random
from Monty_Hall_Analysis import print_values


doors = list(range(5))
trials = 10000
successful_guesses = 0
result_list = []

for i in range(trials):
    car_door = random.choice(doors)
    selected_door = random.choice(doors)
    trial = [selected_door]
    rand_door = random.choice(doors)
    opened_doors = [x for x in doors if x != selected_door and x != rand_door]
    if car_door in opened_doors:
        if car_door != selected_door:
            trial.append(selected_door)
            trial.append(0)
            result_list.append(trial)
            continue
        else:
            trial.append(selected_door)
            successful_guesses += 1
            trial.append(1)
            result_list.append(trial)
            continue
    new_choice = selected_door
    trial.append(new_choice)
    if car_door == new_choice:
        successful_guesses += 1
        trial.append(1)
    else:
        trial.append(0)
    result_list.append(trial)

score = successful_guesses / trials
print(score)

print_values(result_list)