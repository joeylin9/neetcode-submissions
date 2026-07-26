class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def helper(i, action):
            if i >= len(prices):
                return 0
            if (i, action) in dp:
                return dp[(i, action)]

            skip = helper(i + 1, action)
            if action == 'buy':
                buy = helper(i + 1, 'sell') - prices[i]
                dp[(i, action)] = max(buy, skip)
            else:
                sell = helper(i + 2, 'buy') + prices[i]
                dp[(i, action)] = max(sell, skip)
            return dp[(i, action)]

        return helper(0, 'buy')