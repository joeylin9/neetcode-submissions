class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d2 = {}
        for s in strs:
            print(s)
            tupled = tuple(sorted(list(s)))
            if tupled not in d2:
                d2[tupled] = [s]
            else:
                d2[tupled].append(s)
        for k in d2:
            ans.append(d2[k])
        return ans
