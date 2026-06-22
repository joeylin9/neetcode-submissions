class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        counter = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                counter += 1
                seen.add(node)
                queue = [node]
                while queue:
                    cur = queue.pop()
                    for next_node in graph[cur]:
                        if next_node not in seen:
                            seen.add(next_node)
                            queue.append(next_node)
        return counter