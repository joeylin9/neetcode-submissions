class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            ans = numbers[l] + numbers[r]
            if ans<target: # need to go bigger, so shift left up
                l += 1
            elif ans>target:
                r -= 1
            else: #ans == target
                return [l+1, r+1]
        