from sorting_algorithm import *
from prettytable import PrettyTable


def algorithm_runner(array):
    selection = selection_sort(array)
    insertion = insertion_sort(array)
    bubble = bubble_sort(array)
    merge = merge_sort(array)
    quick = quick_sort(array, 0, len(array) - 1)
    radix = radix_sort(array)

    return {
        'selection': {
            'sorted': selection['array'],
            'time': selection['time']
        },
        'insertion': {
            'sorted': insertion['array'],
            'time': insertion['time']
        },
        'bubble': {
            'sorted': bubble['array'],
            'time': bubble['time']
        },
        'merge': {
            'sorted': merge['array'],
            'time': merge['time']
        },
        'quick': {
            'sorted': quick['array'],
            'time': quick['time']
        },
        'radix': {
            'sorted': radix['array'],
            'time': radix['time']
        },
    }


# def test_algorithm(array, case):
#     results = algorithm_runner(array)
#     for algo in results:
#         print(f"Time taken in microseconds for {case} scenario for {algo} sorting is {results[algo]['time']:.3f}")


def test_algorithm(best_case, worst_case):
    best_case = algorithm_runner(best_case)
    worst_case = algorithm_runner(worst_case)
    table = PrettyTable()
    table.field_names = ["Sorting Algorithm", "Best case", "Worst case"]

    table.add_row(["Selection", best_case["selection"]["time"], worst_case["selection"]["time"]])
    table.add_row(["Insertion", best_case["insertion"]["time"], worst_case["insertion"]["time"]])
    table.add_row(["Bubble", best_case["bubble"]["time"], worst_case["bubble"]["time"]])
    table.add_row(["Merge", best_case["merge"]["time"], worst_case["merge"]["time"]])
    table.add_row(["Quick", best_case["quick"]["time"], worst_case["quick"]["time"]])
    table.add_row(["Radix", best_case["radix"]["time"], worst_case["radix"]["time"]])

    return table
