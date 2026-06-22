class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row first
        l, r = 0, len(matrix)-1
        row_i = None
        while l<=r:
            m = (l+r)//2
            if target > matrix[m][len(matrix[m])-1]:
                l = m+1
            elif target < matrix[m][0]:
                r = m-1
            else:
                row_i = m
                break
        
        if row_i is None:
            return False

        row = matrix[row_i]
        l,r = 0, len(row)-1
        while l<=r:
            m = (l+r)//2
            if row[m] > target:
                r = m-1
            elif row[m] < target:
                l = m+1
            else:
                return True
        return False