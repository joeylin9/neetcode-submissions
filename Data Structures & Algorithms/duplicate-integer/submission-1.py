class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            if n in nums[i+1:]:
                return True

        return False