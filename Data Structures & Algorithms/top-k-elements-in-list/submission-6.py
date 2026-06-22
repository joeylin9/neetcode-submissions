class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        freq = [(-counter[n],n) for n in counter]
        heapq.heapify(freq)

        ans = []
        while k:
            ans.append(heapq.heappop(freq)[1])
            k-=1
        return ans
