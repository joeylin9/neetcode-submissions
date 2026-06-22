class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for s in strs:
            freq_arr = [0]*26
            for c in s:
                freq_arr[ord(c)-ord('a')] += 1
            freq_tup = tuple(freq_arr)
            if freq_tup in anagram_dict:
                anagram_dict[freq_tup].append(s)
            else:
                anagram_dict[freq_tup] = [s]
        
        return list(anagram_dict.values())



