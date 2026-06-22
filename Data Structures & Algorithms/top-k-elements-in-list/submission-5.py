class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Have an array of size O(k), since k <= len(nums)
        # Each index of the arr represents a bucket with freq,
        # starting with index 0 having only one instance, index 1 with 2, etc.
        # The last index in the arr has the numbers with the greatest freq
        # create a freq dict and iterate through to add the correct bucket

        tracker = defaultdict(int)
        for n in nums:
            tracker[n] += 1
        bucket_num = max(tracker.values())
        bucket_arr = [[] for _ in range(bucket_num)]

        for n, freq in tracker.items():
            bucket_arr[freq-1].append(n)
        
        ans = []
        added = 0
        pointer = len(bucket_arr)-1
        while added < k:
            while not bucket_arr[pointer]:
                pointer -= 1
            ans.append(bucket_arr[pointer].pop())
            added += 1
        
        return ans

 