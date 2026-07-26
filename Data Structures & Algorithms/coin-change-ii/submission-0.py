class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int) # key is (coin_index, total_left)
        def helper(i, total_left):
            if total_left == 0:
                return 1
            if total_left<0:
                return 0
            if (i, total_left) in dp:
                return dp[(i, total_left)]
            #use same coin
            dp[(i, total_left)] += helper(i, total_left-coins[i])
            #use dif coin
            if i+1 < len(coins):
                dp[(i, total_left)] += helper(i+1, total_left)

            return dp[(i, total_left)]
        return helper(0, amount)
        