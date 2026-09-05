class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        pre = 1
        suf = 1
        for i in range(len(nums)-1):
            pre *= nums[i]
            prefix.append(pre)

            suf *= nums[-i-1]
            suffix.append(suf)
        ans = []
        for i in range(len(prefix)):
            ans.append(prefix[i]*suffix[-i-1])
        return ans