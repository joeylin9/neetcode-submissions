class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += f'({str(len(s))}){s}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
            #figure out count of next word
            i += 1 #starts at first digit of number
            count = ''
            while s[i] != ')':
                count += s[i]
                i += 1

            i += 1 #start at the first letter of the word
            current_word = ''
            for c in range(int(count)):
                current_word += s[i]
                i += 1
            ans.append(current_word)
        return ans



