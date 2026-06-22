class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        memo = {len(nums)-1: nums[-1], len(nums)-2:nums[-2]}
        for i in range(len(nums)-1,-1,-1):
            if i not in memo:
                memo[i] = max(nums[i] + memo[i+2], memo[i+1])
        return memo[0]