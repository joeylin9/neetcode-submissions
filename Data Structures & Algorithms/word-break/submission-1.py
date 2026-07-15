class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        longest = 0
        for c in wordDict:
            longest = max(longest, len(c))

        memo = {}
        def helper(i):
            if i >= len(s):
                memo[i] = True
                return True

            if i not in memo:
                cur = ''
                for j in range(i, i+longest):
                    if j >= len(s):
                        memo[j] = False
                        return False
                    cur += s[j]
                    if cur in wordDict:
                        if helper(j+1):
                            memo[j+1] = True
                            return True
                memo[i] = False
                return False
                
            return memo[i]

        return helper(0)
