class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = set(['(', '{', '['])
        parenthesis = {']': '[', 
                        '}': '{',
                        ')':'('}
        for c in s:
            if c in open_paren:
                stack.append(c)
            else: #end parenthesis
                if not stack or stack[-1] != parenthesis[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0