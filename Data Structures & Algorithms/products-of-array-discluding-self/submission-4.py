class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #3 cases: 0 zeros, 1 zero, >=2 zeroes
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
        
        if zero_count >= 2:
            return [0 for _ in range(len(nums))]
        elif zero_count == 0:
            return [math.prod(nums)//n for n in nums]
        else: # only 1 zero
            nums_copy = nums.copy()
            del nums[nums.index(0)]
            return [0 if n != 0 else math.prod(nums) for n in nums_copy]
