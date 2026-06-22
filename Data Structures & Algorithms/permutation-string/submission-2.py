class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        target = defaultdict(int)
        current = defaultdict(int)
        for i in range(len(s1)):
            target[s1[i]] += 1
            current[s2[i]] += 1
        
        l, r = 0, len(s1)-1
        while r < len(s2):
            if current == target:
                return True

            current[s2[l]] -= 1
            if current[s2[l]] == 0:
                del current[s2[l]]
            l, r = l+1, r+1

            if r >= len(s2):
                return False

            current[s2[r]] += 1

        return False
            
