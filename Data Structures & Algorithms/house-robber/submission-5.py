class Solution:
    def rob(self, nums: List[int]) -> int:
        next1 = 0  # memo[i+1]
        next2 = 0  # memo[i+2]

        for i in range(len(nums) - 1, -1, -1):
            cur = max(nums[i] + next2, next1)
            next2 = next1
            next1 = cur

        return next1