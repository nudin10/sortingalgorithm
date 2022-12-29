from run_algorithm import *
import random
import sys


# Press the green button in the gutter to run the script.
# Fix script: Inaccurate time recording of algorithms
if __name__ == '__main__':
    sys.setrecursionlimit(2500)

    random_array = random.sample(range(1, 10000), 1000)
    best_case = sorted(random_array)
    worst_case = sorted(random_array, reverse=True)

    results = test_algorithm(best_case, worst_case)
    print(results)
