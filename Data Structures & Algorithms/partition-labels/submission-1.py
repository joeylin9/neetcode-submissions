class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = dict()
        start = []
        counter = 0
        ans = []
        for i,c in enumerate(s):
            if c not in seen:
                start.append(i)
                ans.append(1)
                seen[c] = len(ans)
            else: # if seen
                #pop until at index, and add entire new length
                #length of ans should be start + 1
                while len(ans) > seen[c]:
                    start.pop()
                    ans.pop()
                #now ans[-1] is target idx

                for char in seen:
                    if seen[char] >= seen[c]:
                        seen[char] = seen[c]
                ans[-1] = i-start[-1]+1
        return ans