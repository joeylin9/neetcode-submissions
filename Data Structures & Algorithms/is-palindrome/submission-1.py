class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for w in s:
            if w.isalpha() or w.isnumeric():
                l.append(w)
        return l[::-1] == l