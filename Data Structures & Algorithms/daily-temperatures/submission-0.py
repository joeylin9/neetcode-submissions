class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #if greater than first value, set index to diff
                last_index = stack.pop()[1]
                ans[last_index] = i - last_index
            stack.append([t,i])
        return ans