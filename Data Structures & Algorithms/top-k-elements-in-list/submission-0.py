class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        d1 = dict(sorted(d.items(), key=lambda x: x[1], reverse = True))
        ans = []
        a = 0
        for j in d1:
            if a<k:
                ans.append(j)
            a+=1
        return ans