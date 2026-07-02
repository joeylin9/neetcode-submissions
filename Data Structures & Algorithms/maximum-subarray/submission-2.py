class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_all_neg = nums[0]
        all_neg = True
        for n in nums:
            max_all_neg = max(max_all_neg, n)
            if n>0:
                all_neg = False
                break
        if all_neg:
            return max_all_neg

        max_sum = sum(nums)
        l,r = 0, len(nums)-1
        left_sum, right_sum = 0, 0
        while l<=r:
            left_sum += nums[l]
            right_sum += nums[r]
            if left_sum < 0:
                max_sum -= left_sum
                left_sum = 0
            if right_sum < 0:
                max_sum -= right_sum
                right_sum = 0
            l,r = l+1, r-1
        return max_sum
            