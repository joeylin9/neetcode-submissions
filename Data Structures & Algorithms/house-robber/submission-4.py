class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {len(nums)-1: nums[-1], len(nums)-2: max(nums[-1], nums[-2])}
        for i in range(len(nums)-3, -1, -1):
            # take or dont take
            memo[i] = max(nums[i] + memo[i+2], memo[i+1])
        return memo[0]