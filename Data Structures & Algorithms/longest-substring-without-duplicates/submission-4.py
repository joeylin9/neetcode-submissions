class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l,r = 0,1
        longest = 1
        seen = {s[l]: 0}
        while r<len(s):

            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            longest = max(longest, r-l+1)
            seen[s[r]] = r
            r += 1
            
        return longest

