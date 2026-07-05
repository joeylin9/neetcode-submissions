class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        cur_sum = 0

        def helper(cur_sum, i):
            if i >= len(nums):
                return 
            if cur_sum > target:
                return
            elif cur_sum == target:
                ans.append(cur.copy())
                return
            else:
                # take and dont take
                helper(cur_sum, i+1)

                cur_sum += nums[i]
                cur.append(nums[i])
                helper(cur_sum, i)
                cur.pop()
        helper(0, 0)
        return ans
