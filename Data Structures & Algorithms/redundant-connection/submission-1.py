class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_cycle_nodes(graph):
            visited = set()
            parent = {}
            cycle_nodes = set()

            def dfs(node, par):
                visited.add(node)
                parent[node] = par

                for nei in graph[node]:
                    if nei == par:
                        continue

                    if nei in visited:
                        # Found a back edge: node -> nei
                        cur = node
                        cycle_nodes.add(nei)

                        while cur != nei:
                            cycle_nodes.add(cur)
                            cur = parent[cur]

                        return True

                    else:
                        if dfs(nei, node):
                            return True

                return False

            for node in graph:
                if node not in visited:
                    if dfs(node, None):
                        break

            return cycle_nodes

        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        cycles = find_cycle_nodes(graph)
        
        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in cycles and edges[i][1] in cycles:
                return edges[i]
