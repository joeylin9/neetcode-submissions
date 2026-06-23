# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root1, root2):
            if root1 and root2:
                new_root = TreeNode(root1.val + root2.val)
                if root1.left and root2.left:
                    new_root.left = helper(root1.left, root2.left)
                elif not root1.left:
                    new_root.left = root2.left
                elif not root2.left:
                    new_root.left = root1.left

                if root1.right and root2.right:
                    new_root.right = helper(root1.right, root2.right)
                elif not root1.right:
                    new_root.right = root2.right
                elif not root2.right:
                    new_root.right = root1.right   
            elif root1:
                new_root = root1
            elif root2:
                new_root = root2
            else:
                return
            return new_root
        return helper(root1, root2)