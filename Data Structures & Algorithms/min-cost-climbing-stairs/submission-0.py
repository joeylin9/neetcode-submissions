class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def help(cost):
            if len(cost) == 0:
                return 0
            elif len(cost) == 1:
                return cost[0]
            return min(cost[0]+help(cost[1:]), 
            cost[0]+help(cost[2:]))
        
        return min(help(cost[1:]), help(cost[:]))