class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
            
        want = Counter(t)
        have = defaultdict(int)

        for c in want:
            if want[c] > Counter(s)[c]:
                return ''
        
        correct = 0
        l = 0
        ans = (-math.inf,math.inf)
        for i,c in enumerate(s):
            have[c] += 1
            if have[c] == want[c]:
                correct += 1

            while have[s[l]] > want[s[l]]:
                have[s[l]] -= 1
                l += 1
            
            if correct == len(want) and i-l < ans[1] - ans[0]:
                ans = (l, i)

        return s[ans[0]: ans[1]+1]