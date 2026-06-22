class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        
        l,r = 0, 1
        counter = defaultdict(int)
        counter[s[l]] += 1
        max_val = 1
        ans = 1
        while r<len(s):
            counter[s[r]] += 1
            if counter[s[r]] > max_val:
                max_val = counter[s[r]]
            
            #number of need to change is (l-r+1)-max_val
            while (r-l+1)-max_val > k:
                counter[s[l]] -= 1
                l += 1
                if counter[s[r]] > max_val:
                    max_val = counter[s[r]]
            ans = max(ans, r-l+1)
            r += 1
        return ans

