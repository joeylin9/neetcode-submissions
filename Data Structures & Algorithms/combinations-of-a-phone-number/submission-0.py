class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2:'abc', 3:'def', 4:'ghi', 5:'jkl',
            6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
        }
        ans = []
        if not digits:
            return []
        def helper(cur, i):

            if i==len(digits):
                ans.append(cur)
                return
            for l in letters[int(digits[i])]:
                helper(cur+l, i+1)
        helper('', 0)
        return ans