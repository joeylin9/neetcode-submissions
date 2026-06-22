"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        new_node = Node(1)
        new_graph_nodes = {1: new_node}
        seen = set()
        queue = [node]
        new_queue = [new_node]
        while queue:
            cur = queue.pop()
            new_cur = new_queue.pop()
            if cur.val not in seen:
                seen.add(cur.val)
                for n in cur.neighbors:
                    queue.append(n)
                    if n.val not in new_graph_nodes:
                        next_new_cur = Node(n.val) #create new node
                        new_graph_nodes[n.val] = next_new_cur
                    else:  
                        next_new_cur = new_graph_nodes[n.val]
                    new_cur.neighbors.append(next_new_cur)
                    new_queue.append(next_new_cur)

        return new_node

