class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        cur = nums[0]
        for i in range(len(nums)):
            if nums[i] >= cur:
                cur = nums[i]
            if cur <= 0:
                return False
            if i + cur >= len(nums)-1:
                return True
            cur-=1
        return False

