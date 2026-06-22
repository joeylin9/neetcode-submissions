class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        buckets = [[] for _ in range(max(counter.values()))]
        for n in counter:
            buckets[counter[n]-1].append(n)
        pointer = len(buckets)-1
        ans = []
        while k:
            while not buckets[pointer]:
                pointer -= 1
            for n in buckets[pointer]:
                ans.append(n)
                k -= 1
                if k == 0:
                    return ans
            pointer -= 1
        return ans