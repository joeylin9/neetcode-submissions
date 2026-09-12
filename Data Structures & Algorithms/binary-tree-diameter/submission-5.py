# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root, cur):
            nonlocal ans
            if not root:
                return 0
            
            left = helper(root.left, cur+1)
            right = helper(root.right, cur+1)
            ans = max(ans, left + right)
            return 1 + max(left, right)
        helper(root, 1)
        return ans
            




