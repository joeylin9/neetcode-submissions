class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1, 1:1}
        
        def dp(n):
            nonlocal memo

            if n in memo:
                return memo[n]
            else: #one step or two step
                memo[n] = dp(n-2) +  dp(n-1)
                return memo[n]
            
        dp(n)
        return memo[n]
