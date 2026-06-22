class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #go through list
        #first time hitting value: if later, swap if in correct spot, move forth
        #now cur_val is in correct place, but new value may be in wrong place
        #if in right place, keep there and move on to next n
        #else, redo process
        #if swapping w another value that is already in its correct place, that's a duplicate

        for i,n in enumerate(nums):
            cur = nums[i]
            while cur != i+1:
                if nums[cur-1] == cur:
                    return cur
                nums[i], nums[cur-1] = nums[cur-1], cur
                cur = nums[i]
        