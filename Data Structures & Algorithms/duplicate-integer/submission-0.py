class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = []
        for i in nums:
            if i in t:
                return True
            else:
                t.append(i)
        return False