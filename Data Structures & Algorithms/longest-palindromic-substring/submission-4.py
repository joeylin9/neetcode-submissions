class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(l, r):
            nonlocal ans

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # after loop breaks, palindrome is from l+1 to r-1
            cur = s[l + 1:r]

            if len(cur) > len(ans):
                ans = cur

        for i in range(len(s)):
            expand(i, i)       # odd palindrome center
            expand(i, i + 1)   # even palindrome center

        return ans