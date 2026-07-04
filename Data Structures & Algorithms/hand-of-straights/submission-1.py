class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        groups = len(hand) // groupSize
        hand.sort()

        #find the starts
        count = defaultdict(int)
        for n in hand:
            count[n] += 1
        
        starts = []
        for x in hand:
            if count[x] == 0:
                continue
            else:
                starts.append(x)
                for i in range(x, x+groupSize):
                    count[i] -= 1

        target_sum = 0
        for i in starts:
            n = i + (groupSize-1) 
            #i.e. if hand[i] is 1, and groupSize 4, then 1+2+3+4, n = 4
            # use equation, but minus from summation of 1 to hand[i]
            diff_n = i-1
            target_sum += ((n*(n+1))/2) - ((diff_n*(diff_n+1))/2)
        return target_sum == sum(hand)