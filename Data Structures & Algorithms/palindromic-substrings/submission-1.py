class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        def isPalin(i,j):
            if i>=j:
                memo[(i,j)] = True
            if (i,j) not in memo:
                if s[i] == s[j] and isPalin(i+1, j-1):
                    memo[(i,j)] = True
                else:
                    memo[(i,j)] = False

            return memo[(i,j)]

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalin(i,j):
                    count += 1
        return count