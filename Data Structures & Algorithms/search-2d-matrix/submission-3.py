class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the correct row
        # look at the last value
        t,b = 0, len(matrix)-1
        while t<b:
            m = (t+b+1)//2
            if matrix[m][0] <= target: #target is less than so lower the row
                t=m
            else:
                b=m-1
        l,r = 0, len(matrix[t])-1
        while l<=r:
            m = (l+r)//2
            if matrix[b][m] == target:
                return True
            elif matrix[b][m] > target:
                r = m-1
            else:
                l = m+1
        return False
