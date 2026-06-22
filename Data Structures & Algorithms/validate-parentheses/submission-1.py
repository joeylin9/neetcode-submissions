class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {']': '[', 
                        '}': '{',
                        ')':'('}
        for c in s:
            if c in parenthesis:
                if not stack or stack[-1] != parenthesis[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0