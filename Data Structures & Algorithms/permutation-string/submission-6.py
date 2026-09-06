class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        want = Counter(s1)
        have = defaultdict(int)
        correct = 0
        l = 0
        for i, c in enumerate(s2):
            have[c] += 1
            if have[c] == want[c]:
                correct += 1
            elif have[c] == want[c]+1:
                correct -= 1

            while have[s2[l]] > want[s2[l]]:
                have[s2[l]] -= 1
                if have[s2[l]] == want[s2[l]]:
                    correct += 1
                l += 1
                if l >= len(s2):
                    return False
            
            if correct == len(want):
                return True
                
        return False