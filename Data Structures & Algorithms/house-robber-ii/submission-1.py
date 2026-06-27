class Solution:
    def rob(self, nums: List[int]) -> int:
        # take or dont take the last, if dont take, can take first
        def dfs(i, first_taken, memo):
            if i >= len(nums):
                return 0
            
            if i == len(nums)-1 and not first_taken:
                memo[i] = nums[-1]
            elif i == len(nums)-1 and first_taken:
                memo[i] = 0
            
            if i not in memo:
                memo[i] = max(nums[i] + dfs(i+2, first_taken, memo), dfs(i+1, first_taken, memo))

            return memo[i]
        
        memo1, memo2 = {0: 0}, {0: nums[0]} #dont take, take
        take_first = nums[0] + dfs(2, True, {})
        dont_take_first = dfs(1, False, {})
        return max(take_first, dont_take_first)
        
