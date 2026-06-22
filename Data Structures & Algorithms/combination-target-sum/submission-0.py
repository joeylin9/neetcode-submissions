class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        cur_sum = 0

        def helper(i):
            nonlocal cur_sum, cur, ans

            #take i or dont
            if i >= len(nums) or cur_sum > target:
                return
            
            if cur_sum == target:
                ans.append(cur.copy())
                return
            
            helper(i+1) # dont take

            #take
            cur_sum += nums[i]
            cur.append(nums[i])
            helper(i)

            cur_sum -= nums[i]
            cur.pop()
        
        helper(0)
        return ans