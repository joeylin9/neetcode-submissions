# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val
        def in_order_traversal(root):
            nonlocal count, res

            if root.left:
                in_order_traversal(root.left)

            if count == 0:
                return
            count -= 1
            if count == 0:
                res = root.val
                return

            if root.right:
                in_order_traversal(root.right)
        in_order_traversal(root)
        return res