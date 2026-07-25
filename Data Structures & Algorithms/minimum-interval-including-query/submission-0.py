class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = sorted([(q, i) for i,q in enumerate(queries)], key = lambda x: x[0])
        intervals.sort()
        interval_idx = 0
        # print(queries)
        
        heap = [] # min heap of (length, end)
        for query_i in range(len(queries)):
            cur_query, query_idx = queries[query_i]
            # print(f'this is cur query {cur_query}, and query index {query_idx}, with query being {queries[query_i]}')

            # add in valid intervals
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= cur_query:
                cur_interval = intervals[interval_idx]
                heapq.heappush(heap, (cur_interval[1]-cur_interval[0]+1, cur_interval[1]))
                interval_idx += 1

            # remove invalid intervals
            while heap and heap[0][1] < cur_query:
                heapq.heappop(heap)
            
            if heap:
                length = heap[0][0]
            else:
                length = -1

            queries[query_i] = (cur_query, query_idx, length)

        # print(queries)

        i = 0
        while i < len(queries):
            if isinstance(queries[i], tuple):
                _, index, length = queries[i]
                if i != index:
                    queries[i], queries[index] = queries[index], length
                else:
                    queries[i] = length
            #if not a tuple, length is already placed correctly
            else:
                i += 1
        return queries


            