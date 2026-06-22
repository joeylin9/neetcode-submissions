class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word))+'#'+word
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        left = 0
        while left < len(s):
            hash_idx = s.find('#', left)
           
            length = int(s[left:hash_idx])
        
            start = hash_idx + 1
            word = s[start:start + length]
            l.append(word)
            
            left = start + length
        
        return l