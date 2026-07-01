class WordDictionary:

    def __init__(self):
        self.children = dict() #letter to another dict of children
        self.endWord = False

    def addWord(self, word: str) -> None:
        cur = self
        prev = None
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            prev, cur = cur, cur.children[c]
        prev.endWord = True

    def search(self, word: str) -> bool:
        def helper(cur, i):
            if i == len(word)-1 and cur.endWord and (word[i] in cur.children or word[i] == '.'):
                return True
            elif i == len(word)-1:
                return False

            c = word[i]
            if c == '.':
                return any([helper(cur.children[x], i+1) for x in cur.children])
            elif c not in cur.children:
                return False
            else:
                return helper(cur.children[c], i+1)
        
        return helper(self, 0)
