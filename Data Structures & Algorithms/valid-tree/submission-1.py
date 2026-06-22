class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree is valid if
        # 1. there are no loops
        # 2. there are n-1 edges
        # 3. the tree is connected

        # build a graph (tree)
        # go thorugh all possible paths using bfs or dfs
        # keep prev for one bfs level, if neighbor == prev, pass, else if in seen:
        # there is a loop, return false
        # check if len(seen) == n, check if n-1 edges
    
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        seen = {0}
        queue = [(0, math.inf)]
        while queue:
            node, prev = queue.pop()
            seen.add(node)
            neighbors = graph[node]
            for nb in neighbors:
                if nb in seen and nb!=prev:
                    return False
                if nb!=prev:
                    queue.append((nb, node))
                    
        return True if len(seen) == n else False
                
