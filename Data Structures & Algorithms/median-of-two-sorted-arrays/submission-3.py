class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # a is bigger, b is smaller
        if len(nums1) > len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        
        total_len = len(a) + len(b)
        half_len = total_len // 2

        # binary search number of elements from b on the left
        l, r = 0, len(b)

        while l <= r:
            b_left_len = (l + r) // 2
            a_left_len = half_len - b_left_len

            # boundary values
            b_left = b[b_left_len - 1] if b_left_len > 0 else float("-inf")
            b_right = b[b_left_len] if b_left_len < len(b) else float("inf")

            a_left = a[a_left_len - 1] if a_left_len > 0 else float("-inf")
            a_right = a[a_left_len] if a_left_len < len(a) else float("inf")

            # correct partition
            if b_left <= a_right and a_left <= b_right:
                if total_len % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2

            # b_left is too big, move b partition left
            elif b_left > a_right:
                r = b_left_len - 1

            # a_left is too big, move b partition right
            else:
                l = b_left_len + 1