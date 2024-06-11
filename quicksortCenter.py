def partition(arr, low, high, pivot):
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    return low


def anotherQuickSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        pivot = arr[mid]

        n = partition(arr, low, high, pivot)
        anotherQuickSort(arr, low, n - 1)
        anotherQuickSort(arr, n, high)


if __name__ == '__main__':
    my_arr = [7, 14, 6, 1, 3, 8, 11, 12, 9, 0, 12, 23, 40, 10]
    anotherQuickSort(my_arr, 0, len(my_arr) - 1)
    for i in my_arr:
        print(i, end=" ")
