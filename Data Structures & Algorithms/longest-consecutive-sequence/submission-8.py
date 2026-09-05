class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            cur_len = 1
            next_num = n+1
            if n-1 not in nums:
                while next_num in nums:
                    cur_len += 1
                    next_num += 1
            ans = max(ans, cur_len)
        return ans