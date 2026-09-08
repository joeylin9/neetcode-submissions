class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from functools import reduce

        l,r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            time = reduce(lambda x,pile_amount: x+math.ceil(pile_amount/m), piles, 0)
            if time <= h: #can still try to decrease
                r = m
            else:
                l = m+1
        return r
