class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        #find the starts
        count = defaultdict(int)
        for n in hand:
            count[n] += 1
        
        for x in hand:
            if count[x] == 0:
                continue
            else:
                for i in range(x, x+groupSize):
                    count[i] -= 1
                    if count[i] < 0:
                        return False
        return True