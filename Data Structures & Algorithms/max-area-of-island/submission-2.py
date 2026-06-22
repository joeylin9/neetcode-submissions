class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        seen = set()

        def neighbors(coord):
            """Return valid neighbors (within bounds and == 1)"""
            dirs = [(0,1), (0,-1), (1,0), (-1,0)] # right, left, down, up
            neighbs = []
            for d in dirs:
                new_coord = (coord[0]+d[0], coord[1]+d[1])
                if 0<=new_coord[0]<len(grid) and 0<=new_coord[1]<len(grid[0]) and grid[new_coord[0]][new_coord[1]] == 1:
                    neighbs.append(new_coord)
            return neighbs

        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if (row_i, col_i) not in seen and grid[row_i][col_i] == 1:
                    cur = (row_i, col_i)
                    seen.add(cur)
                    cur_area = 1
                    queue = [cur]
                    while queue:
                        cur = queue.pop()
                        for n in neighbors(cur):
                            if n not in seen:
                                seen.add(n)
                                cur_area += 1
                                queue.append(n)
                    area = max(cur_area, area)
        return area


