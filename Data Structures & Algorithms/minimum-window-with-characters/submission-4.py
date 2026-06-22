class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # at c, if in target and equals target already, then shift the window
        # to the next earliest letter in target
        # if ==, put as ans and check length every time

        def equal(x, y):
            if len(x.keys()) != len(y.keys()):
                return False
            for c in x:
                if x[c] < y[c]:
                    return False
            return True

        target = defaultdict(int)
        current = defaultdict(int)
        ans = ''
        ans_length = math.inf
        indices = []
        l = 0
        invalid_letters = set(t)

        for c in t:
            target[c] += 1

        r = 0
        while r < len(s):
            if s[r] in target:
                current[s[r]]+=1
                indices.append(r)

                if s[r] in invalid_letters and current[s[r]] >= target[s[r]]:
                    invalid_letters.remove(s[r])

            if not invalid_letters:
                while not invalid_letters:

                    if r + 1 - l < ans_length:
                        ans = s[l:r+1]
                        ans_length = r + 1 - l

                    if s[l] in target:
                        current[s[l]] -= 1

                        if current[s[l]] < target[s[l]]:
                            invalid_letters.add(s[l])
                    l += 1

            r+=1

        return ans
