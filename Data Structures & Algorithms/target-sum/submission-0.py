class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #key is (i,target)
        def helper(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            
            dp[(i,target)] = helper(i+1, target-nums[i]) + helper(i+1, target+nums[i])
            return dp[(i,target)]

        return helper(0, target)