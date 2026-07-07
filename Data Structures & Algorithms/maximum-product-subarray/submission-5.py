class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = -math.inf
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[len(nums) - 1 - i]

            ans = max(ans, prefix, suffix)

        return ans