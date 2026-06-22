class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            print(stack)
            try: # c is an int
                stack.append(int(c))
            except:
                print(c)
                if c == '+':
                    stack.append(stack.pop(-2) + stack.pop(-1))
                if c == '-':
                    stack.append(stack.pop(-2) - stack.pop(-1))
                if c == '*':
                    stack.append(stack.pop(-2) * stack.pop(-1))
                if c == '/':
                    dividend = stack.pop(-2) / stack.pop(-1)
                    if dividend >= 0:
                        dividend = math.floor(dividend)
                    else:
                        dividend = math.ceil(dividend)

                    stack.append(dividend)

        return stack[0]