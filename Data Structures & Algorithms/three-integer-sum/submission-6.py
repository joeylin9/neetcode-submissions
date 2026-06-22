class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i,n in enumerate(nums):
            target = -n
            l,r = i+1, len(nums)-1
            while l<r:
                cur_sum = nums[l] + nums[r]
                if cur_sum<target:
                    l += 1
                elif cur_sum>target:
                    r -= 1
                else:
                    ans.add((n, nums[l], nums[r]))
                    l,r = l+1, r-1
        
        return list(ans)
                