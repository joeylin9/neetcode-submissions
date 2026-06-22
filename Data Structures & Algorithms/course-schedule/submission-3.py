class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make a graph
        #if cycle, return false
        sources = set(range(numCourses))
        graph = defaultdict(list) #node: [neighbors]
        for a,b in prerequisites:
            if a == b:
                return False
            graph[b].append(a)
            sources.discard(a)
        if not sources:
            return False
        print(graph)

        for s in sources:
            seen = {s}
            queue = [s]
            while queue:
                cur = queue.pop()
                if cur not in graph:
                    continue
                seen.add(cur)
                for n in graph[cur]:
                    if n in seen:
                        return False
                    queue.append(n)
        return True
                    
