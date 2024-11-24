import math
def main():
    arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    n = len(arr)

    quick_sort(arr, 0, n - 1)

    for i in arr:
        print(i, end=" ")
    print()

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return i
    
    
main()
