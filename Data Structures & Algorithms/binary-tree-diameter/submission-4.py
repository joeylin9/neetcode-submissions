# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0

            return 1+max(helper(root.left), helper(root.right))
        
        ans = 0
        def helper2(root):
            nonlocal ans
            if not root:
                return 0
            
            ans = max(ans, helper(root.right)+helper(root.left))
            helper2(root.left)
            helper2(root.right)
        
        helper2(root)
        return ans



