class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # First element in preorder is the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            root_idx_in_inorder = inorder_map[root_val]
            left_subtree_size = root_idx_in_inorder - in_start
            
            # build left and right subtrees
            root.left = helper(
                pre_start + 1,
                pre_start + left_subtree_size,
                in_start,
                root_idx_in_inorder - 1
            )
            
            root.right = helper(
                pre_start + left_subtree_size + 1,
                pre_end,
                root_idx_in_inorder + 1,
                in_end
            )
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)