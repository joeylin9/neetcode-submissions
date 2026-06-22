class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            nonlocal seen, visiting, ans, graph, has_cycle
            if has_cycle:
                return
            if node in visiting: # loop
                has_cycle = True
                return
            if node in seen:
                return
                
            visiting.add(node)
            if node in graph:
                for n in graph[node]:
                    dfs(n)
            visiting.remove(node)
            seen.add(node)
            ans.append(node)
            return

        graph = defaultdict(list)
        sources = set(range(numCourses))
        for a,b in prerequisites:
            graph[b].append(a)
            sources.discard(a)
            
        seen = set()
        visiting = set()
        has_cycle = False
        ans = []
        for s in sources:
            if s not in seen:
                dfs(s)  
        if has_cycle:
            return []
        ans.reverse()
        return ans
