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
            return None

        d = {}
        d[node] = Node(node.val)

        visited = set()
        agenda = [node]

        while agenda:
            current = agenda.pop()
            ns = current.neighbors
            for n in ns:
                if n not in visited:
                    d[n] = Node(n.val)
                    agenda.append(n)
                    visited.add(n)
                d[current].neighbors.append(d[n])
        return d[node]

