class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # need tuple of (frequency, number)
        freq_arr = []
        for n in freq:
            freq_arr.append((-freq[n], n))
        heapq.heapify(freq_arr)

        return [heapq.heappop(freq_arr)[1] for _ in range(k)]