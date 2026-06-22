class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def help(i):
            if i >= len(nums):
                return 0
            
            if i not in memo:
                memo[i] = max(nums[i] + help(i+2), help(i+1))
            return memo[i]
        
        return help(0)