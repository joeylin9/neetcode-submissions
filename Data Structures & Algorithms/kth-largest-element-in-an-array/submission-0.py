class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numbers = []
        heapq.heapify(numbers)

        for n in nums:
            heapq.heappush(numbers, n)
            while len(numbers) > k:
                heapq.heappop(numbers)
        
        return numbers[0]