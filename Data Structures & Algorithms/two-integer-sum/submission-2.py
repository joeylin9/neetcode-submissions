class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in memo:
                return [memo[diff], i]
            
            memo[n] = i