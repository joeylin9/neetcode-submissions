class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_low, k_high = 1, max(piles)
        
        while k_low <= k_high:
            k = (k_low+k_high)//2
            time = 0
            for b in piles:
                time += math.ceil(b/k)
            
            if time>h: #took too long, shorten by increasing k
                k_low = k+1
            else: # time<h: finished quick, can try shortening k for optimization
                k_high = k-1
                k_shortest = k

        return k_shortest