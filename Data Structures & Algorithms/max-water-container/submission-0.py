class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights)-1

        while l < r:
            height = min(heights[l], heights[r])
            width = r-l
            cur_area = width * height
            area = max(area, cur_area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return area