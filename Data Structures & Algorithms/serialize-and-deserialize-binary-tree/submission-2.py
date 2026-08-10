# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        nodes = []
        def dfs(cur):
            if cur:
                nodes.append(str(cur.val))
                dfs(cur.left)
                dfs(cur.right)
            else:
                nodes.append('None')
        dfs(root)
        return '.'.join(nodes)
        

    def deserialize(self, data):
        if data == 'None':
            return 

        tree = data.split('.')

        def helper(node):
            nonlocal i

            if i >= len(tree):
                return

            value = tree[i]
            if value == 'None':
                pass
            else:
                node.left = TreeNode(int(value))
                i+=1
                helper(node.left)
            
            i+=1

            if i >= len(tree):
                return

            value = tree[i]
            if value == 'None':
                pass
            else:
                node.right = TreeNode(int(value))
                i+=1
                helper(node.right)
                
        root = TreeNode(int(tree[0]))
        i = 1
        helper(root)
        return root


            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))