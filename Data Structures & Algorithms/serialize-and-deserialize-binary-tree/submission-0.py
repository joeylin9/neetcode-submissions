# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ''

        def helper(queue):
            nonlocal ans
            next_queue = collections.deque()
            while queue:
                cur = queue.popleft()
                if cur:
                    ans += '.' + str(cur.val)
                    next_queue.append(cur.left)
                    next_queue.append(cur.right)
                else:
                    ans += '.Null'
                helper(next_queue)
        
        helper(collections.deque([root]))
        return ans[1:]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'Null':
            return
        
        values = data.split('.')
        values = collections.deque(values)

        head_val = int(values.popleft())
        head = TreeNode(head_val)
        root = head
        def helper(root):
            left = values.popleft()
            if left == 'Null':
                pass
            else:
                root.left = TreeNode(int(left))
                helper(root.left)

            right = values.popleft()
            if right == 'Null':
                pass
            else:
                root.right = TreeNode(int(right))
                helper(root.right)
                
        helper(root)
        return head
        

            