class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        ans = 0
        l, r = 0,0
        while r<len(s):
            if s[r] not in chars:
                chars.add(s[r])
                ans = max(ans, r-l+1)
                r+=1
            else:
                # char is already in, so restart
                while s[r] in chars:
                    chars.remove(s[l])
                    l+=1
        return ans

