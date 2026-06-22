# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_subtree(root, subroot):
            """
            Check if current root is the subtree
            """
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            return check_subtree(root.left, subroot.left) and check_subtree(root.right, subroot.right)
        if not root and not subRoot:
            return False
        if not root or not subRoot:
            return False
        
        return check_subtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

           