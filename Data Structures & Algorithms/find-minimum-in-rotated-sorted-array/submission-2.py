class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def find(l, r):
            m = (l+r)//2

            #if theres a decrease from the first to last, the kink is there
            if nums[l] > nums[m]:
                #its on the left side
                return find(l, m)
            elif nums[m+1] > nums[r]:
                # its on the right side
                return find(m+1,r)
            else:
                #either in the middle of the two or in the beginning
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    return nums[m+1]
                
        
        l, r = 0, len(nums)-1
        return find(l,r)
        

