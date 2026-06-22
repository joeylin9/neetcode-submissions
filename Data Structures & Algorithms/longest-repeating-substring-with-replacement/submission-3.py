class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,1
        freq = {s[l]: 1}
        max_freq = 1
        ans = 1

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(max_freq, freq[s[r]])

            number_replacements = (r-l+1)-max_freq
            if number_replacements > k:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
            r += 1
        
        return ans