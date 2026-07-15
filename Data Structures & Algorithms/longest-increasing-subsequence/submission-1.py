class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {len(nums)-1: 1}
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if i in memo:
                        memo[i] = max(memo[i], 1 + memo[j])
                    else:
                        memo[i] = 1+memo[j]
            
            if i not in memo:
                memo[i] = 1

        return max(memo.values())