class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur = 0
        ans = 0
        for i, tup in enumerate(zip(gas,cost)):
            g,c = tup
            cur += g
            cur -= c
            if cur < 0:
                cur = 0
                ans = i+1
        return ans