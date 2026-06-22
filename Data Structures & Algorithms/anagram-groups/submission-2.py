class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d2 = defaultdict(list)
        for s in strs:
            tupled = tuple(sorted(list(s)))
            d2[tupled].append(s)
        return d2.values()
