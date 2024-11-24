import math
def main():
    arr = [8, 2, 5, 3, 4, 7, 6, 1]

    merge_sort(arr)
    for i in arr:
        print(i, end=" ")
    print()

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return #base case 
    
    mid = math.floor(n / 2)
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr, right_arr, arr)

def merge(left_arr, right_arr, arr):
    l = 0
    r = 0
    i = 0
    left_size = len(left_arr)
    right_size = len(right_arr)

    while (l < left_size) and (r < right_size):
        if left_arr[l] < right_arr[r]:
            arr[i] = left_arr[l]
            i += 1
            l += 1
        else:
            arr[i] = right_arr[r]
            r += 1
            i += 1
    while l < left_size:
        arr[i] = left_arr[l]
        i += 1
        l += 1
    while r < right_size:
        arr[i] = right_arr[r]
        i += 1
        r += 1
main()