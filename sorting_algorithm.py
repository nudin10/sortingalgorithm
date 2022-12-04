import time
from utils import *


def selection_sort(arr):
    # Selection sort in Python
    # time complexity O(n*n)
    # auxiliary space O(1)
    # sorting by finding min_index

    start_t = time.perf_counter()
    for ind in range(len(arr)):
        min_index = ind

        for j in range(ind + 1, len(arr)):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    start_t = time.perf_counter()
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}


def bubble_sort(arr):
    start_t = time.perf_counter()
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}


def merge_sort(arr):
    start_t = time.perf_counter()
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}


def quick_sort(arr, low, high):
    start_t = time.perf_counter()
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        # recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)

    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}


def radix_sort(arr):
    start_t = time.perf_counter()

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10

    end_t = time.perf_counter()
    ms = (end_t - start_t) * 10**6
    return {'array': arr, 'time': ms}
