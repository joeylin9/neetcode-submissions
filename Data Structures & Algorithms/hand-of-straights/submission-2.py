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
                    if count[i] < 0:
                        return False
        return True