class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_copy = nums[:]
        for i in range(len(nums)):
            prod = 1
            for x in range(len(nums_copy)):
                if x!=i:
                    prod *= nums_copy[x]
            nums[i] = prod
        return nums