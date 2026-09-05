class Solution:

    def encode(self, strs: List[str]) -> str:
        counts = []
        for s in strs:
            counts.append(len(s))
        res = []
        for count, s in zip(counts, strs):
            res.append(f'{count}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i<len(s):
            num = []
            while s[i] != '#':
                num.append(s[i])
                i+=1
            i+=1
            num = int(''.join(num))

            word = []
            for _ in range(num):
                word.append(s[i])
                i+=1
            word = ''.join(word)
            ans.append(word)
        return ans

