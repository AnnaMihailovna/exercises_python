def binarySearch(arr, x, left, right):
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)

arr = [1, 2, 3, 4, 5, 6, 7, 11, 15, 25, 29, 34, 56]
x = 3
# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearch(arr, x, left = 0, right = len(arr))
print(index)
