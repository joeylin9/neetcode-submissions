class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalin(s):
            """Checks if a string s is a palindrome"""
            l,r = 0, len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l,r = l+1,r-1
            return True
            
        def helper(i, cur_s, cur_palins):            
            if i == len(s):
                if cur_s == '':
                    ans.append(list(cur_palins.copy()))
                return
            cur_s += s[i]

            #if palindrome, put it in the current
            if isPalin(cur_s):
                cur_palins.append(cur_s)
                helper(i+1, '', cur_palins)
                cur_palins.pop()

            helper(i+1, cur_s, cur_palins)

        helper(0, '', [])
        return ans