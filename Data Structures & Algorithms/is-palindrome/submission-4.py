class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True