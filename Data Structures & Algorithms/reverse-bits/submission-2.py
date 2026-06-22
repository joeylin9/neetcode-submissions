class Solution:
    def reverseBits(self, n: int) -> int:
        s = f"{n:032b}"
        s = s[::-1]
        return int(s, 2)