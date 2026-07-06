class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # at each step, if any value is over target, return False
        # if all three are under target, do operation
        # at end, if all three are target, return True
        t1, t2, t3 = target
        i = 0
        cur = None
        while i < len(triplets):
            val1,val2,val3 = triplets[i]
            if val1<=t1 and val2<=t2 and val3<=t3:
                cur = triplets[i]
                break
            i+=1
        if not cur:
            return False

        for j in range(i+1, len(triplets)):
            val1,val2,val3 = triplets[j]
            if val1>t1 or val2>t2 or val3>t3:
                continue
            else:
                cur = [max(val1, cur[0]), max(val2, cur[1]), max(val3, cur[2])]
        
        val1,val2,val3 = cur
        return val1==t1 and val2==t2 and val3==t3
