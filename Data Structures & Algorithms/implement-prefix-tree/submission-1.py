class PrefixTree:

    def __init__(self):
        self.root = ''
        self.children = {}
        self.endWord = False

    def insert(self, word: str) -> None:
        def helper(tree, i):
            if i >= len(word):
                tree.endWord = True
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
                cur.endWord = True
        helper(self, 0)

    def search(self, word: str) -> bool:
        i = 0
        cur = self
        while i<len(word):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
                i+=1
            else:
                return False
        return cur.endWord

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
        