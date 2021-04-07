import random
import matplotlib.pyplot as plt
import seaborn as sns
from Monty_Hall_Analysis import print_values

result_list = []
for_plot = []

def simulation():
    doors = list(range(100))
    trials = 200
    successful_guesses = 0

    for i in range(trials):
        car_door = random.choice(doors)
        selected_door = random.choice(doors)
        trial = [selected_door]
        available_doors = [x for x in doors if x != selected_door and x != car_door]
        opened_doors = random.sample(available_doors, len(doors) - 2)
        new_choice = [x for x in doors if x not in opened_doors if x != selected_door][0]
        trial.append(new_choice)
        if car_door == new_choice:
            successful_guesses += 1
            trial.append(1)
        else:
            trial.append(0)
        result_list.append(trial)

    score = successful_guesses / trials
    return score

def mean():
    sample = []
    for i in range(1000):
        sample.append(simulation())
    sns.displot(sample, bins = 20)
    print(sum(sample) / len(sample))
    plt.show()

simulation()
print_values(result_list)
mean()



