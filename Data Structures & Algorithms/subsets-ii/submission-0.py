class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def helper(i, cur, prev):
            if i>=len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            helper(i+1, cur, nums[i])
            cur.pop()
            if nums[i] != prev:
                helper(i+1, cur, prev)
        helper(0, [], math.inf)
        return ans