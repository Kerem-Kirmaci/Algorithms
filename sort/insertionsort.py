def main():
    arr = [6, 1, 7, 4, 2, 9, 8, 5, 3]
    n = len(arr)

    insertion_sort(arr, n)

    for i in arr:
        print(i, end=" ")
    print()

def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

main()
        

