# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            """
            return False if left and right children not balanced
            else returns the total nodes of the entire tree from root
            including root
            """
            if not root.right and not root.left:
                return 1

            left_len = helper(root.left) if root.left else 0
            right_len = helper(root.right) if root.right else 0

            if right_len is False or left_len is False:
                return False
            if abs(left_len - right_len) > 1:
                return False
            else:
                return 1 + max(left_len,right_len)
        
        if not root:
            return True
        ans = helper(root)
        return ans if ans == False else True
