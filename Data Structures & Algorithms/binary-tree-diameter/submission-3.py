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
                left_len = longest_len(root.left)
                right_len = longest_len(root.right)
                self.diameter = max(self.diameter, left_len+right_len)
                return 1+max(left_len, right_len)

        self.diameter = 0
        longest_len(root)
        return self.diameter

