class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list) #pattern to words, i.e. "*ag": [sag, bag, dag]
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        if beginWord == endWord:
            return 0
        
        def neighbors(word):
            neighs = []
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighs += graph[pattern]
            return neighs

        level = 1
        queue = [beginWord]
        seen = {beginWord}
        while queue:
            level += 1
            next_queue = []
            for word in queue:
                for n in neighbors(word):
                    if n not in seen:
                        if n == endWord:
                            return level
                        seen.add(n)
                        next_queue.append(n)
            queue = next_queue
        return 0
            