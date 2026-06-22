class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += word+'~'
        return s
    def decode(self, s: str) -> List[str]:
        l = []
        left = 0
        for i,c in enumerate(s):
            if c == '~':
                l.append(s[left:i])
                left = i+1
        return l
