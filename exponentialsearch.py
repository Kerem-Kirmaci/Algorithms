def main():
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    target = "h"
    n = len(arr)
    value = expo_search(arr, target, n - 1)

    if value == -1:
        print("Letter is not in the array!")
    else:
        print(f"Letter is in the array at the index: {value}")

def expo_search(arr, target, n):
    if arr[0] == target:
        return 0
    i = 1
    temp = 0
    
    while arr[i] <= target:
        if arr[i] == target:
                return i
        elif temp == i:
            return -1
        else:
            if (i * 2) < n:
                temp = i
                i *= 2
            else: 
                temp = i
                i = n
    return binary_search(arr, temp, i, target)

def binary_search(arr, low, high, target):
    

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
main()
