class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {len(cost)-1: cost[-1], len(cost)-2: cost[-2]}
        for i in range(len(cost)-3,-1,-1):
            if i not in memo:
                memo[i] = cost[i] + min(memo[i+1], memo[i+2])
        print(memo)
        return min(memo[0], memo[1])