def merge_segments(segments_sort):
    start, end = segments_sort[0]
    index_next_segment = 1
    flower_beds = []
    while index_next_segment < len(segments_sort):
        next_start, next_end = segments_sort[index_next_segment]
        if (start <= next_start <= end or
                start <= next_end <= end):
            start, end = min(start, next_start), max(end, next_end)
        else:
            flower_beds.append([start, end])
            start, end = segments_sort[index_next_segment]
        index_next_segment += 1
    flower_beds.append([start, end])

    return flower_beds


# def merge_sort(segments):
#     if len(segments) == 1:
#         return segments

#     left = merge_sort(segments[0: len(segments) // 2])
#     right = merge_sort(segments[len(segments) // 2: len(segments)])

#     segments_sort = [] * len(segments)

#     l, r = 0, 0

#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             segments_sort.append(left[l])
#             l += 1
#         else:
#             segments_sort.append(right[r])
#             r += 1

#     while l < len(left):
#         segments_sort.append(left[l])
#         l += 1
#     while r < len(right):
#         segments_sort.append(right[r])
#         r += 1

#     return segments_sort


def main():
    gardens = int(input())
    segments = [[int(i) for i in input().split()] for garden in range(gardens)]
    # flower_beds = merge_segments(merge_sort(segments))
    segments_sort = sorted(segments)
    flower_beds = merge_segments(segments_sort)
    [print(*i) for i in flower_beds]


if __name__ == '__main__':
    main()
