class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum//2

        def helper(i, cur):
            if cur > target or i == len(nums):
                return False
            elif cur == target:
                return True
            else:
                return helper(i+1, cur+nums[i]) or helper(i+1, cur)
        
        return helper(0, 0)