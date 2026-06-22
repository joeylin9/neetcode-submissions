class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        res = [1 for i in nums]
        prefix = 1
        for i,n in enumerate(nums):
            res[i] = prefix
            prefix*=n
        #postfix
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res