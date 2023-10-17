def sift_down(heap, idx) -> int:
    l = 2 * idx
    r = 2 * idx + 1
    if len(heap) - 1 >= l:
        if (r <= len(heap) - 1) and (heap[l] < heap[r]):
            idx_largest = r
        else:
            idx_largest = l
        if heap[idx] < heap[idx_largest]:
            heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
            return sift_down(heap, idx_largest)
    return idx

# def sift_down(heap, idx) -> int:
#     l = 2 * idx
#     r = 2 * idx + 1
#     while (len(heap) - 1) >= l:
#         if (r <= len(heap) - 1) and (heap[l] < heap[r]):
#             idx_largest = r
#         else:
#             idx_largest = l
#         if heap[idx] < heap[idx_largest]:
#             heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
#             # sift_down(heap, idx_largest)
#             return idx_largest
#     if idx <= len(heap) - 1:
#         return idx
        

# def test():
#     sample = [-1, 12, 1, 8, 3, 4, 7]
#     assert sift_down(sample, 2) == 5

# def test():
#     sample = [12, 9, 6, 2, 4, 1]
#     print(sift_down(sample, 8))

# if __name__ == '__main__':
#     test()
