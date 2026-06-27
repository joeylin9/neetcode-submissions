class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # for each int, either take or dont
        # if take, output k-1, else just k
        # at end if k == 0, return that ans, else dont

        def helper(i, cur):
            if i >= len(nums):
                ans.append(cur)
                return
            
            helper(i+1, cur) # dont take
            helper(i+1, [nums[i]]+cur) # take
        helper(0, [])
        return ans
            