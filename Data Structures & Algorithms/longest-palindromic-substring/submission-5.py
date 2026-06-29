class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        memo = {}
        max_start = 0
        max_len = 1
        
        def is_palindrome(i, j):
            # Base cases
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Substring s[i...j] is a palindrome only if boundary matches
            # AND the inner substring s[i+1...j-1] is also a palindrome
            if s[i] == s[j] and is_palindrome(i + 1, j - 1):
                memo[(i, j)] = True
            else:
                memo[(i, j)] = False
                
            return memo[(i, j)]
        
        # Evaluate all possible substrings to find the longest palindrome
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        max_start = i
                        
        return s[max_start : max_start + max_len]
