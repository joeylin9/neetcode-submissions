class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for s in strs:
            if len(s) in d:
                d[len(s)].append(s)
            else:
                d[len(s)] = [s]
        for key in d:
            d2 = {}
            for word in d[key]:
                sorted_list = sorted(list(word))
                tupled = tuple(sorted_list)
                if tupled not in d2:
                    d2[tupled] = [word]
                else:
                    d2[tupled].append(word)
            for k in d2:
                ans.append(d2[k])
        return ans
