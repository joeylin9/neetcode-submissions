class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            s = str(n)
            n = 0
            for c in s:
                n += int(c)**2
            if n in seen:
                return False
            seen.add(n)
        return True