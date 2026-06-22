class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, n**2)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap))
        return ans