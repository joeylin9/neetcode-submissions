class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(row_i, col_i):
            dirs = [(-1,0), (1,0), (0,1), (0,-1)] # up, down, right, left
            neighbors = []
            for d in dirs:
                next_coord = (row_i + d[0], col_i + d[1])
                if 0<=next_coord[0]<len(grid) and 0<=next_coord[1]<len(grid[0]):
                    neighbors.append(next_coord)
            return neighbors

        seen = set()
        islands = 0
        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if (row_i, col_i) not in seen and grid[row_i][col_i] == '1':
                    queue = [(row_i, col_i)]
                    seen.add((row_i, col_i))
                    while queue:
                        cur = queue.pop()
                        for n in neighbors(cur[0], cur[1]):
                            if n not in seen:
                                seen.add(n)
                                if grid[n[0]][n[1]] == '1':
                                    queue.append(n)
                    # once queue ends, island is found, all around is 0s
                    islands += 1
                # seen.add((row_i, col_i))
        return islands