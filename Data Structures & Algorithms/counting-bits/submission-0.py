class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = {0:0, 1:1}
        def helper(n):
            if n in dp:
                return dp[n]
            
            if n > 0 and (n&(n-1) == 0):
                dp[n] = 1
            else:
                two_power = 1 << (n.bit_length()-1)
                dp[n] = helper(two_power) + helper(n-two_power)
            return dp[n]
        return [helper(i) for i in range(n+1)]

