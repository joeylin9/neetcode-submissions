"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        cur = head
        cur_node_dict = {} # node to nodeid
        new_node_dict = {} # nodeid to newcur
        new_head = Node(head.val)
        new_cur = new_head

        node_id = 0
        while cur:
            if not cur.next:
                new_cur.next = None
            else:
                new_cur.next = Node(cur.next.val)
            cur_node_dict[cur] = node_id
            new_node_dict[node_id] = new_cur
            
            new_cur = new_cur.next
            cur = cur.next
            node_id += 1

        cur = head
        new_cur = new_head
        while cur:
            random_node_id = cur_node_dict.get(cur.random, None)
            new_random_node = new_node_dict.get(random_node_id, None)

            new_cur.random = new_random_node
            new_cur = new_cur.next
            cur = cur.next

        return new_head


        


