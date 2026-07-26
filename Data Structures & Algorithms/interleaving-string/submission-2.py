class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {} #key being (i,j) where i is index in s1 and j is for s2
        s_count, t_count = 0, 0
        building = None
        
        def helper(i,j,k,new_build): #k is index in s3
            nonlocal s_count, t_count, building
            if (i,j) in dp:
                return dp[(i,j)]

            if new_build and (building is None or building != new_build):
                building = new_build
                if new_build == 'i':
                    s_count += 1
                else:
                    t_count += 1

            if k == len(s3):
                return abs(s_count-t_count)<=1 and i == len(s1) and j == len(s2)

            if i >= len(s1) and j >= len(s2):
                return False
            elif i >= len(s1): #j is still left
                if s2[j] != s3[k]:
                    return False
                dp[(i,j)] = helper(i,j+1,k+1,'j')
            elif j >= len(s2): # i is still left
                if s1[i] != s3[k]:
                    return False
                dp[(i,j)] = helper(i+1,j,k+1,'i')
            elif s3[k] == s1[i] and s3[k] == s2[j]:
                dp[(i,j)] = helper(i+1,j,k+1,'i') or helper(i,j+1,k+1,'j')
            elif s3[k] == s1[i]: #using i
                dp[(i,j)] = helper(i+1,j,k+1,'i')
            elif s3[k] == s2[j]:
                dp[(i,j)] = helper(i,j+1,k+1,'j')
            else:
                return False
            return dp[(i,j)]
        
        return helper(0,0,0,None)