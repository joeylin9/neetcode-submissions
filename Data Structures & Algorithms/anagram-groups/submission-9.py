class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = Counter(s)
            key = [0] * 26
            for letter in count:
                key[ord(letter)-ord('a')] = count[letter]
            key = tuple(key)
            anagrams[key].append(s)
        return list(anagrams.values())

            