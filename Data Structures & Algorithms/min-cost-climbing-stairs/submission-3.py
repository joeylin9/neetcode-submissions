class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1 = cost[-2]  # memo[i+1]
        next2 = cost[-1]  # memo[i+2]

        for i in range(len(cost) - 3, -1, -1):
            cur = cost[i] + min(next1, next2)
            next1, next2 = cur, next1

        return min(next1, next2)