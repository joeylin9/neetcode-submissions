class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}  # key -> node
        self.cap = capacity

        # dummy nodes
        # left is most recent side
        # right is least recent side
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_front(self, node):
        first_node = self.left.next

        node.prev = self.left
        node.next = first_node

        self.left.next = node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]

        # since we used it, move it to most recent position
        self.remove(node)
        self.insert_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            # update existing node
            node = self.d[key]
            node.val = value

            # move it to most recent position
            self.remove(node)
            self.insert_front(node)

        else:
            # create new node
            node = Node(key, value)
            self.d[key] = node
            self.insert_front(node)

            # if too many, remove least recently used
            if len(self.d) > self.cap:
                lru_node = self.right.prev
                self.remove(lru_node)
                del self.d[lru_node.key]