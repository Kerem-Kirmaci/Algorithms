def main():
    arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    n = len(arr)

    bubble_sort(arr, n)
    
    for i in arr:
        print(f"{i}",end=" ")
    print()

def bubble_sort(arr, n):
    change = True
    while change:
        change = False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                change = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        n -= 1        
            
main()