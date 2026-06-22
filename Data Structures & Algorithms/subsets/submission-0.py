class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        # for each int, either take or dont
        # if take, output k-1, else just k
        # at end if k == 0, return that ans, else dont

        def helper(i, k, cur):
            if k == 0:
                ans.append(cur)
                return True
            if k>len(nums)-i or i >= len(nums): # [1,2,3,(4,5)] but k = 3, i = 3, len = 5: 5-3 = 2
                return False

            #dont take
            helper(i+1, k, cur)
            
            #take
            cur1 = cur + [nums[i]]
            next_iter = helper(i+1, k-1, cur1)
            if not next_iter: 
                return
        
        for k in range(length+1):
            helper(0, k, [])
        return ans
            