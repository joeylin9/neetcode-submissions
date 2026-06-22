# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def input(queue):
            if not queue or not queue[0]:
                return

            next_queue = collections.deque()
            level = []
            while queue:
                node = queue.popleft()
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                level.append(node.val)
            ans.append(level)
            input(next_queue)
        
        ans = []
        input(collections.deque([root]))
        return ans
            
            