class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
            
        want = Counter(t)
        have = defaultdict(int)
        
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
                if l==len(s):
                    return ''
            
            if correct == len(want) and i-l < ans[1] - ans[0]:
                ans = (l, i)

        return '' if ans[0] == -math.inf or ans[1] == math.inf else s[ans[0]: ans[1]+1]