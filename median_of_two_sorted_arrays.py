from typing import List, Tuple
# если убрат импорт, тогда проходит в яндекс.контесте

def read_input() -> Tuple[int, int, List[int], List[int]]:
    n = int(input())
    m = int(input())
    north = [int(i) for i in input().split()]
    south = [int(i) for i in input().split()]
    return n, m, north, south

def get_median(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    len1, len2 = len(nums1), len(nums2)
    len_total = len1 + len2
    len_half = len_total // 2
    nums1_lptr, nums1_rptr = 0, len1 - 1
    while True:
        nums1_mptr = (nums1_lptr + nums1_rptr) // 2
        nums2_mptr = len_half - nums1_mptr - 2

        nums1_mid_left_val = nums1[nums1_mptr] if nums1_mptr >= 0 else float("-inf")
        nums1_mid_right_val = nums1[nums1_mptr + 1] if (nums1_mptr + 1) < len1 else float("+inf")
        nums2_mid_left_val = nums2[nums2_mptr] if nums2_mptr >= 0 else float("-inf")
        nums2_mid_right_val = nums2[nums2_mptr + 1] if (nums2_mptr + 1) < len2 else float("+inf")

        if (
            nums1_mid_left_val <= nums2_mid_right_val and
            nums2_mid_left_val <= nums1_mid_right_val 
        ):
            if len_total%2 == 0:
                return (
                    max(nums1_mid_left_val, nums2_mid_left_val) +
                    min(nums1_mid_right_val, nums2_mid_right_val)
                ) / 2
            else:
                return min(nums1_mid_right_val, nums2_mid_right_val)
        else:
            if nums1_mid_left_val > nums2_mid_right_val:
                nums1_rptr = nums1_mptr - 1
            else:
                nums1_lptr = nums1_mptr + 1


def main() -> None:
    _, _, north, south = read_input()
    print(get_median(north, south))


if __name__ == '__main__':
    main()
