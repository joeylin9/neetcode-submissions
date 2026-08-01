class Solution:
    def reverseBits(self, n: int) -> int:
        #reversing goes to 31-i
        ans = 0
        for i in range(32):
            # check if set
            if n & (1<<i): #it is set
                ans = ans | (1<<31-i)
        return ans