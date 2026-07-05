class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(left, right, cur):
            #either add a right or dont
            if left == 0:
                while right:
                    cur += ')'
                    right-=1
                ans.append(cur)
                return

            if right == 0:
                ans.append(cur)
                return

            if left < right:
                helper(left, right-1, cur + ')') #take right
                # or dont take right

            helper(left-1, right, cur + '(')

        helper(n, n, '')
        return ans