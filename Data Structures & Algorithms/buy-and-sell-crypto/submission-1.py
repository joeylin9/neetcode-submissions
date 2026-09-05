class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        ans = 0
        for p in prices:
            ans = max(ans, p-buy)
            if p < buy:
                buy = p
        return ans
