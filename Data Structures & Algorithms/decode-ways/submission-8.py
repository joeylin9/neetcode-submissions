class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def helper(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            #now can always take one digit
            memo[i] = helper(i+1)

            #can only two two digits if the two together are from 10-26
            if i+1 < len(s) and 10<=int(s[i] + s[i+1])<=26:
                memo[i] += helper(i+2)
            
            return memo[i]

        return helper(0)
