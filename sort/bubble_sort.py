"""
Алгоритм состоит из повторяющихся проходов по сортируемому массиву. За каждый проход
элементы последовательно сравниваются попарно и, если порядок в паре неверный,
выполняется перестановка элементов. Проходы по массиву повторяются N-1 раз или до тех пор,
пока на очередном проходе не окажется, что обмены больше не нужны,
что означает — массив отсортирован. При каждом проходе алгоритма по внутреннему циклу
очередной наибольший элемент массива ставится на своё место в конце массива рядом с
предыдущим «наибольшим элементом», а наименьший элемент перемещается на одну позицию
к началу массива («всплывает» до нужной позиции, как пузырёк в воде — отсюда и название алгоритма).
"""
def bubble(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble([11, 2, 9, 7, 1]))
