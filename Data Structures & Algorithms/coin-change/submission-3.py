class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        memo = {}
            
        def helper(amount):
            if amount < 0:
                return math.inf
            elif amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            # try with every coin

            memo[amount] = min(1 + helper(amount-c) for c in coins)
            return memo[amount]
                
        result = helper(amount)
        return -1 if result == math.inf else result
