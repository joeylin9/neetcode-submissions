class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # tuple of anagram, list of words that is anagram
        for s in strs:
            ana = [0]*26
            for c in s:
                ana[ord(c)-ord('a')] += 1
            d[tuple(ana)].append(s)
        return list(d.values())