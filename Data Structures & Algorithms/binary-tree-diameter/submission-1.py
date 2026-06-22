# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longest_len(root):
            if not root:
                return 0
            else:
                return 1+max(longest_len(root.left), longest_len(root.right))
        if not root:
            return 0
        return max(longest_len(root.left) + longest_len(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))