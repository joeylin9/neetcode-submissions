class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            ana = sorted(list(str))
            d[tuple(ana)].append(str)
        return list(d.values())
