class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            needed = target - n
            if needed in d.keys():
                return [d[needed],i]
            else:
                d[n] = i