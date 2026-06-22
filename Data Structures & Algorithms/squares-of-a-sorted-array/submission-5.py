class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_value, min_index = math.inf, 0
        for i, n in enumerate(nums):
            nums[i] = n**2
            if n**2 < min_value:
                min_value = n**2
                min_index = i

        ans = []
        l = min_index
        r = min_index+1
        while l>=0 or r<len(nums):
            if r>=len(nums) or (l>=0 and nums[l]<= nums[r]):
                ans.append(nums[l])
                l-=1
            elif l<0 or (r<len(nums) and nums[l] > nums[r]):
                ans.append(nums[r])
                r+=1
        return ans