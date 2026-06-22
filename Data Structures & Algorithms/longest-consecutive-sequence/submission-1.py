class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        tempans = 1
        temp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == temp:
                continue
            if nums[i] == temp+1:
                tempans += 1
            else:
                ans = max(tempans, ans)
                tempans = 1
            temp = nums[i]
        return max(tempans, ans)
