class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = n**2

        ans = []
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l]>= nums[r]:
                ans.append(nums[l])
                l+=1
            else:
                ans.append(nums[r])
                r-=1
        ans.reverse()
        return ans