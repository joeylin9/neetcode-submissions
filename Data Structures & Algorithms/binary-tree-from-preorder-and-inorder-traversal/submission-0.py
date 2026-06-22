# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # value -> index in inorder
        inorder_index = {val: i for i, val in enumerate(inorder)}
        preorder_i = 0

        def build(left, right):
            nonlocal preorder_i

            # no nodes in this inorder range
            if left > right:
                return None

            # preorder gives root first
            root_val = preorder[preorder_i]
            preorder_i += 1

            root = TreeNode(root_val)

            # split inorder around root
            mid = inorder_index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)