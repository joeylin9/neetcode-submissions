class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #0,1,2,3,5
        # 000, 001, 010, 011, 101
        # xor: 001, 011, 000, 101
        # xor with 4: 101 ^ 100 = 001
        # xor both: 100

        res = 0
        for i in range(len(nums)+1):
            res ^= i
        
        for n in nums:
            res ^= n
        
        return res