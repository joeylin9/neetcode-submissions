class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            key = tuple(key)
            anagrams[key].append(s)
        return list(anagrams.values())

            