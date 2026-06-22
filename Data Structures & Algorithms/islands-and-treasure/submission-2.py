class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def get_neighbors(coord):
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            neighbors = []
            for d in dirs:
                new_coord = (coord[0]+d[0], coord[1]+d[1])
                if 0<=new_coord[0]<len(grid) and 0<=new_coord[1]<len(grid[0]):
                    neighbors.append(new_coord)
            return neighbors

        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if cell == 0:
                    seen = set((row_i, col_i))
                    queue = [(row_i, col_i)]
                    level = 1
                    while queue:
                        next_queue = []
                        for coord in queue:
                            for n in get_neighbors(coord):
                                val = grid[n[0]][n[1]]
                                if n not in seen and val != -1 and val != 0:
                                    seen.add(n)
                                    grid[n[0]][n[1]] = min(grid[n[0]][n[1]], level)
                                    next_queue.append(n)
                        level += 1
                        queue = next_queue

                                    
