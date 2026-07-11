class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = 0
        paren_stack = []
        star_stack = []
        for i,c in enumerate(s):
            if c == '*':
                star_stack.append(i)
            elif c == '(':
                paren_stack.append(i)
            elif c == ')':
                if not paren_stack:
                    if not star_stack:
                        return False
                    else:
                        star_stack.pop()
                else:
                    paren_stack.pop()
        while paren_stack:
            if not star_stack or paren_stack.pop() > star_stack.pop():
                return False
        return True