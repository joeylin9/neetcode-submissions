class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = {}
        a2 = {}
        for c in s:
            if c in a1:
                a1[c] += 1
            else:
                a1[c] = 1
        for c in t:
            if c in a2:
                a2[c] += 1
            else:
                a2[c] = 1

        return a1==a2
        