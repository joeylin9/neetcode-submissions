class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        pointer = {}
        for n in nums:
            if n in pointer:
                next_bucket = pointer[n] + 1
                buckets[pointer[n]].remove(n)
            else:
                next_bucket = 0
            pointer[n] = next_bucket
            if next_bucket+1 > len(buckets):
                buckets.append(set())
            buckets[next_bucket].add(n)
        ans = []
        pointer = len(buckets)-1
        while k:
            while not buckets[pointer]:
                pointer-=1
            ans.append(buckets[pointer].pop())
            k-=1
        return ans

