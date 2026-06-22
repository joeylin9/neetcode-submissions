class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        ans = 1
        l,r = 0, 1
        prev_l = 0
        seen = {s[l]: 0}
        while r<len(s):
            print(f'looking at word {s[l:r+1]}')
            if s[r] in seen:
                l = max(prev_l, seen[s[r]] + 1)
                prev_l = l             
            ans = max(ans, r-l+1)
            seen[s[r]] = r
            r+=1
        return ans