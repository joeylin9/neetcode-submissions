# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(root, output):
            if root.left:
                in_order_traversal(root.left, output)
            output.append(root.val)
            if root.right:
                in_order_traversal(root.right, output)
            return output

        output = in_order_traversal(root, [])
        return output[k-1]