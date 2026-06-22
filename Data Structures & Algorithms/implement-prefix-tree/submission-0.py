class PrefixTree:

    def __init__(self):
        self.root = ''
        self.children = defaultdict(list)
        self.added = set()

    def insert(self, word: str) -> None:
        def helper(tree, i):
            if i >= len(word):
                return

            if word[i] in tree.children:
                helper(tree.children[word[i]], i+1)
            else: #create new tree
                cur = tree
                while i<len(word):
                    child = PrefixTree()
                    child.root = word[i]
                    cur.children[word[i]] = child
                    cur = child
                    i+=1
        self.added.add(word)
        helper(self, 0)

    def search(self, word: str) -> bool:
        return word in self.added

    def startsWith(self, prefix: str) -> bool:
        i = 0
        cur = self
        while i<len(prefix):
            if prefix[i] in cur.children:
                cur = cur.children[prefix[i]]
                i+=1
            else:
                return False
        return True
        