class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            
            count = 0
            for p in piles:
                count += math.ceil(p/m)
            
            if count <= h:
                r = m
            else:
                l = m+1
        return r
