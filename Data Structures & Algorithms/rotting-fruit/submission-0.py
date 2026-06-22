class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def neighbors(coord):
            dirs = [(0,1), (0,-1), (-1,0), (1,0)]
            neighs = []
            for d in dirs:
                new = (d[0]+coord[0], d[1]+coord[1])
                if 0<=new[0]<len(grid) and 0<=new[1]<len(grid[0]):
                    neighs.append(new)
            return neighs
        
        sources = []
        count = 0
        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if cell == 2:
                    sources.append((row_i, col_i))
                if cell == 1:
                    count+=1
        
        queue = sources
        time = 0
        counter = 0
        seen = set(sources)
        while queue:
            next_queue = []
            for coord in queue:
                for n in neighbors(coord):
                    if grid[n[0]][n[1]] == 1 and n not in seen:
                        seen.add(n)
                        counter += 1
                        next_queue.append(n)
            queue = next_queue
            if queue:
                time+=1
        return time if counter == count else -1