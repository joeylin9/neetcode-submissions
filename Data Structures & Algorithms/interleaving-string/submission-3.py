class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def helper(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j
            dp[(i, j)] = False

            if i < len(s1) and s1[i] == s3[k]:
                dp[(i, j)] = helper(i + 1, j)

            if not dp[(i, j)] and j < len(s2) and s2[j] == s3[k]:
                dp[(i, j)] = helper(i, j + 1)

            return dp[(i, j)]

        return helper(0, 0)