import random
import matplotlib.pyplot as plt
import seaborn as sns
from Monty_Hall_Analysis import print_values

result_list = []

def simulation():
    doors = list(range(100))
    trials = 10000
    successful_guesses = 0

    for i in range(trials):
        car_door = random.choice(doors)
        selected_door = random.choice(doors)
        trial = [selected_door]
        new_choice = selected_door
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