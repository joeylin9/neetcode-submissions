class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l, r = 0, len(nums)-1

        def binsearch(l,r):
            while l<=r:
                m = (l+r)//2
                if nums[m]<target:
                    l = m+1
                elif nums[m]>target:
                    r = m-1
                else:
                    return m
            return -1

        while l<=r:
            m = (l+r)//2
            if nums[m+1] == nums[r]: #only one index on the right side
                if nums[r] == target:
                    return r
                else:
                    r = m

            elif nums[m+1] > nums[r]: #kink on the right
                #check left side if it is within
                if nums[l] <= target <= nums[m]:
                    return binsearch(l,m)
                else: #its on the right, do it again
                    l = m+1

            elif nums[l] > nums[m]: # kink on the left
                #check right side if it is within
                if nums[m+1] <= target <= nums[r]:
                    return binsearch(m+1, r)
                else:
                    r = m

            else: #kink in the middle or no kink at all
                return max(binsearch(l,m), binsearch(m+1, r))

        return -1