
def bantuan(arr, low, high):
    # menentukan pivot
    pivot = arr[high]

    # menentukan i = index awal - 1
    i = low - 1

    # menentukan j = index awal
    # menjalankan perulangan
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

            # temp = arr[i]
            # arr[i] = arr[j]
            # arr[j] = temp

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # temp = arr[i + 1]
    # arr[i + 1] = arr[high]
    # arr[high] = temp

    # return
    return i + 1


def quicksort(arr: list, low: int, high: int):
    if low < high:
        n = bantuan(arr, low, high)

        quicksort(arr, low, n - 1)
        quicksort(arr, n + 1, high)


if __name__ == '__main__':
    my_arr = [2, 4, 1, 5, 3]

    panjang = len(my_arr)
    quicksort(my_arr, 0, panjang - 1)

    for k in my_arr:
        print(k, end=" ")
