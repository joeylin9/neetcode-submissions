class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest_times = {node_id: math.inf for node_id in range(1,n+1)} #dictionary of nodes to shortest time to get to node
        shortest_times[k] = 0
        graph = defaultdict(list)
        edge_lengths = {}

        for n1,n2,t in times:
            graph[n1].append(n2)
            edge_lengths[(n1,n2)] = t
        
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, k))
        while queue: 
            time, cur = heapq.heappop(queue)
            for n in graph[cur]:
                new_time = shortest_times[cur] + edge_lengths[(cur, n)]
                if new_time < shortest_times[n]:
                    heapq.heappush(queue, (new_time, n))
                    shortest_times[n] = shortest_times[cur] + edge_lengths[(cur, n)]
        ans = max(shortest_times.values())
        return -1 if ans == math.inf else ans