def main():
    arr = [1,2,3,4,5,6]
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    for i in arr:
        print(i, end=" ")
    print()

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    
    if left < n and arr[left] > arr[largest]:
        largest = left

    
    if right < n and arr[right] > arr[largest]:
        largest = right

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)


main()