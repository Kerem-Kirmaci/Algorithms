def main():
    arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    n = len(arr)

    selection_sort(arr, n)

    for i in arr:
        print(i, end=" ")
    print()

def selection_sort(arr, n):
    
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
main()
