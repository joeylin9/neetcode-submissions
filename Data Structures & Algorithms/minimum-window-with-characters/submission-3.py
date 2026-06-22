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

        for c in t:
            target[c] += 1

        r = 0
        while r < len(s):
            if s[r] in target:
                current[s[r]]+=1
                indices.append(r)

            if equal(current, target):
                while equal(current, target):
                    first = indices[0]

                    if r + 1 - first < ans_length:
                        ans = s[first:r+1]
                        ans_length = r + 1 - first

                    first = indices.pop(0)
                    current[s[first]] -= 1 

            r+=1
            print(current)
            print()

        return ans
