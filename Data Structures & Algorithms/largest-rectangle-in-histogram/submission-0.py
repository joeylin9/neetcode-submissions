class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_boundary = [len(heights)] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            if stack and h < stack[-1][0]:
                while stack and h<stack[-1][0]:
                    right_boundary[stack.pop()[1]] = i
            stack.append((h,i))

        left_boundary = [-1]*len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if stack and h < stack[-1][0]:
                while stack and h<stack[-1][0]:
                    left_boundary[stack.pop()[1]] = i
            stack.append((h,i))
        return max([h* (right_boundary[i]-left_boundary[i]-1) for i,h in enumerate(heights)])

                