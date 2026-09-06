class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # keep the colder temps
        ans = [-1] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                ans[index] = i-index
            stack.append([t, i])
        while stack:
            temp, index = stack.pop()
            ans[index] = 0
        return ans

