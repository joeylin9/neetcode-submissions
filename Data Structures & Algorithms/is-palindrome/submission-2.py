class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for w in s:
            if w.isalnum():
                l.append(w)
        return l[::-1] == l