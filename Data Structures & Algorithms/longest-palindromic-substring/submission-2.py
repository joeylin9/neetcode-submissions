class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_length = 1
        ans = s[0]
        for i in range(len(s)):
            cur = s[i]
            l,r = i-1,i+1
            while l >= 0 and r<=len(s)-1:
                if s[l]==s[r]:
                    cur = s[l] + cur + s[r]
                    if len(cur) >= longest_length:
                        longest_length = len(cur)
                        ans = cur
                    l,r = l-1, r+1
                else:
                    break

        for i in range(len(s)):
            cur = ''
            l,r = i,i+1
            while l >= 0 and r<=len(s)-1:
                if s[l]==s[r]:
                    cur = s[l] + cur + s[r]
                    if len(cur) >= longest_length:
                        longest_length = len(cur)
                        ans = cur
                    l,r = l-1, r+1
                else:
                    break
        return ans