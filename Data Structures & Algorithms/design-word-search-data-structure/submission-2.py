class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endWord = False

    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]

        cur.endWord = True

    def search(self, word: str) -> bool:
        def helper(cur, i):
            if i == len(word):
                return cur.endWord

            c = word[i]

            if c == '.':
                for child in cur.children.values():
                    if helper(child, i + 1):
                        return True
                return False

            if c not in cur.children:
                return False

            return helper(cur.children[c], i + 1)

        return helper(self, 0)