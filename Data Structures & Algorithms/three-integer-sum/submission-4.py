class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = None
        ans = []

        for i, n in enumerate(nums):
            if n == seen:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum < -n:
                    l  += 1
                    continue
                elif _sum > -n:
                    r -= 1
                    continue
                else: #equals
                    ans.append([n, nums[l], nums[r]])
                    seen = n
                    while r-1>=0 and nums[r-1] == nums[r]:
                        r-=1
                    l,r = l+1, r-1
        return ans
