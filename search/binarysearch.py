import math

def main():
    arr = ["a","b","c","d","e","f","g","h","i","j","k"]
    target = "c"
    value = -1
    n = len(arr)
    value = binarySearch(arr, n, target)

    if value != -1:
        print(f"{target} is in the index: {value}")
    else:
        print('Letter is not in the array')

def binarySearch(arr, n, target):
    if(n == 0):
        return -1
    else:
        low = 0
        high = n - 1
        mid = math.floor((low + high) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr[:mid], n - mid - 1, target)
        elif arr[mid] < target:
            return binarySearch(arr[mid+1:], n - mid - 1, target)
main()