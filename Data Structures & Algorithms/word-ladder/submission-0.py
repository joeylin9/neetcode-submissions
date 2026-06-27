class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for word2 in wordList:
                change = 0
                for c1,c2 in zip(word, word2):
                    if c1 != c2:
                        change += 1
                if change == 1:
                    graph[word].append(word2)
        
        if beginWord == endWord:
            return 0

        level = 1
        queue = [beginWord]
        seen = {beginWord}
        while queue:
            level += 1
            next_queue = []
            for word in queue:
                for n in graph[word]:
                    if n not in seen:
                        if n == endWord:
                            return level
                        seen.add(n)
                        next_queue.append(n)
            queue = next_queue
        return 0
            