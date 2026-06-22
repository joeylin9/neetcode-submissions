class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [-n for n in nums]
        ans = []
        l, r = 0, k
        window = nums[0:k]
        heapq.heapify(window)

        freq = defaultdict(int)
        max_val = math.inf
        for n in range(r):
            max_val = min(max_val, nums[n])
            freq[nums[n]] += 1

        ans.append(-max_val)
        freq[nums[l]] -= 1
        l += 1

        while r < len(nums):

            heapq.heappush(window, nums[r]) # add next value
            freq[nums[r]] += 1

            while freq[window[0]] == 0:
                heapq.heappop(window)

            ans.append(-window[0])

            freq[nums[l]] -= 1
            l,r = l+1, r+1
    
        return ans