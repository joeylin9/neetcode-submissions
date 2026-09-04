class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        for num in freqs:
            heapq.heappush(heap, (freqs[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]