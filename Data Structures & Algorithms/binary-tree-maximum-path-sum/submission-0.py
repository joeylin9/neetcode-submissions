# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #every node will have tuple (max_assuming_root, left_max+val or just val, right_max+val or just val)
        def helper(root) -> tuple:
            if not root.left and not root.right: # leaf
                return (root.val, root.val, root.val)
            if root.left:
                l = helper(root.left)
                leftMax = max(root.val + max(l[1], l[2]), root.val)
            else:
                l = ()
                leftMax = root.val
            if root.right:
                r = helper(root.right)
                rightMax = max(root.val + max(r[1], r[2]), root.val)
            else:
                rightMax = root.val

            if not root.right:
                pathMax = max(max(l), leftMax)
            elif not root.left:
                pathMax = max(max(r), rightMax)
            else:
                pathMax = max(max(l), max(r), leftMax, rightMax, root.val + max(l[1], l[2]) + max(r[1], r[2]))
            return (pathMax, leftMax, rightMax)
        return max(helper(root))
