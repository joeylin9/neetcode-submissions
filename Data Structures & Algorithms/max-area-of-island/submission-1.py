class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_neighbors(i1, i2):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            temp_list = []
            
            for di, dj in directions:
                ni, nj = i1 + di, i2 + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] == 1:
                    temp_list.append((ni, nj))
    
            return temp_list

        visited = set()
        island_sizes = [0]
        for rowi, row in enumerate(grid):
            for coli, col in enumerate(row):
                if col == 1 and (rowi, coli) not in visited:
                    agenda = [(rowi, coli)]
                    size = 1
                    visited.add((rowi, coli))
                    while agenda:
                        i1, i2 = agenda.pop()
                        neighbors = get_neighbors(i1,i2)
                        for n in neighbors:
                            if n not in visited:
                                size += 1
                                agenda.append(n)
                                visited.add(n)
                    island_sizes.append(size)
        return max(island_sizes)
                


