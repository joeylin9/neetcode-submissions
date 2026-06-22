class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find(l, r):
            if l == r:
                return nums[l]

            m = (l+r)//2

            #if theres a decrease from the first to last, the kink is there
            if nums[m] > nums[r]:
                # its on the right side
                return find(m+1,r)
            else:
                return find(l, m)
                
        
        l, r = 0, len(nums)-1
        return find(l,r)
        

