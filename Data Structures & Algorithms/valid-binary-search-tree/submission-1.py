# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min_val, max_val):
            if not root:
                return True
            
            if not min_val < root.val < max_val:
                return False
            
            left_valid, right_valid = True, True
            if root.right:
                min_val2 = root.val
                right_valid = helper(root.right, min_val2, max_val)
            if root.left:
                max_val2 = root.val
                left_valid = helper(root.left, min_val, max_val2)
            
            return right_valid and left_valid

        return helper(root, -math.inf, math.inf)