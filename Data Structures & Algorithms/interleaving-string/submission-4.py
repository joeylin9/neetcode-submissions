class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {} #key being (i,j) where i is index in s1 and j is for s2
        
        def helper(i,j,k): #k is index in s3
            if (i,j) in dp:
                return dp[(i,j)]

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            dp[(i, j)] = False
            if i < len(s1) and s1[i] == s3[k]: # use i
                dp[(i, j)] = helper(i+1, j, k+1)
            if not dp[(i, j)] and j < len(s2) and s2[j] == s3[k]: # if i didnt work, try j
                dp[(i, j)] = helper(i, j+1, k+1)
            return dp[(i, j)]
        
        return helper(0,0,0)