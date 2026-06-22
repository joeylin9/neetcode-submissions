class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        for i,n in enumerate(nums):
            if n-1 not in nums:
                temp = 1
                tempans = 1
                while n+temp in nums:
                    tempans+=1
                    temp+=1
                ans = max(tempans,ans)
        return ans