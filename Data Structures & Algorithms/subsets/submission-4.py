class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(cur, i):
            if i >= len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            helper(cur, i+1)
            cur.pop()
            helper(cur, i+1)
        
        helper([], 0)
        return ans