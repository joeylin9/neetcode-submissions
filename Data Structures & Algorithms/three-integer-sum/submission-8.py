class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i=0
        while i<len(nums):
            n = nums[i]
            l,r = i+1, len(nums)-1
            target = -n
            while l<r:
                if nums[l]+nums[r] == target:
                    ans.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l+=1
                    while r>=0 and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r] < target:
                    l += 1
                else:
                    r -= 1
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
        return ans