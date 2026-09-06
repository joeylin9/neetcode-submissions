class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = defaultdict(int)
        max_count = 0
        other_count = 0
        ans = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            if freqs[s[r]] > max_count:
                max_count = freqs[s[r]]
            else:
                other_count += 1
            while other_count > k:
                # if freqs[s[l]] == max_count:
                #     max_count -= 1
                # else:
                other_count -= 1

                freqs[s[l]] -= 1
                if freqs[s[l]] == 0:
                    del freqs[s[l]]
                l += 1

            ans = max(ans, r-l+1)
        return ans
            