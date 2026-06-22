class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = {'a':0, 'b':1, 'c':2,'d':3, 'e':4, 'f':5,'g':6, 
        'h':7, 'i':8,'j':9, 'k':10, 'l':11,'m':12, 'n':13, 
        'o':14,'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 
        'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

        anagram_dict = {}

        for s in strs:
            freq_arr = [0]*26
            for c in s:
                freq_arr[alpha_dict[c]] += 1
            freq_tup = tuple(freq_arr)
            if freq_tup in anagram_dict:
                anagram_dict[freq_tup].append(s)
            else:
                anagram_dict[freq_tup] = [s]
        
        return list(anagram_dict.values())
