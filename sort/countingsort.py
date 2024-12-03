import array
def main():
    arr = [1, 3, 2, 9, 7, 0, 1, 5]
    n = len(arr)

    arr = counting_sort(arr)

    for i in arr:
        print(i, end=" ")
    print()

def counting_sort(arr):
    length_of_count = max(arr)

    

    count = array.array('i', [0] * (length_of_count + 1))
    arr_new = arr[:]
    for i in arr:
        count[i] += 1
    for i in range(1, length_of_count + 1):
        count[i] = count[i - 1] + count[i]
    for i in arr:
        arr_new[count[i] - 1 ] = i
        count[i] -= 1
    return arr_new

main()

    