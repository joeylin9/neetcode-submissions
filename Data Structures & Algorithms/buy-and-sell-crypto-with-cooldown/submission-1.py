class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #take or dont take, sell or dont sell
        #2d dp where i is buy, and j is sell, j>i
        dp = {}
        def helper(i):
            if i>=len(prices):
                return 0
            if i in dp:
                return dp[i]
            
            #take i
            max_sell = 0
            for j in range(i+1, len(prices)):
                max_sell = max(max_sell, prices[j] + helper(j+2))
            dp[i] = max(-prices[i] + max_sell, helper(i+1))
            return dp[i]
        return helper(0)