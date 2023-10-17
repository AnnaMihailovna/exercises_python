def binarySearchDescending(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x: # искомый элемент больше центрального
        # на этот раз все элементы больше центрального
        # располагаются в левой половине
        return binarySearchDescending(arr, x, left, mid)
    else:
        return binarySearchDescending(arr, x, mid + 1, right)

arr = [1, 2, 3, 4, 5, 6, 7, 11, 15, 25, 29, 34, 56]
arr = arr[::-1]
print(arr)
x = 3
# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearchDescending(arr, x, left = 0, right = len(arr))
print(index)
