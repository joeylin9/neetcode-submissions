class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l,r = 0, 0
        count = 0
        while r < len(nums)-1:
            next_r = r
            for i in range(l,r+1):
                next_r = max(next_r, i + nums[i])
            l,r = r+1, next_r
            count += 1
        return count
        