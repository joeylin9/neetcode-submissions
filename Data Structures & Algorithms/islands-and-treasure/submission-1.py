class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find 0s
        # perform bfs from the 0s, replacing a land cell if current step number is less than the land cell val
        # step number is the number of steps (bfs) from the 0

        # find 0s 
        zeros = []

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    zeros.append((i,j))
        
        def find_neighbors(coord):
            neighbors = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #up down left right
            for d in directions:
                new_row = coord[0] + d[0]
                new_col = coord[1] + d[1]
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] >= 1:
                    neighbors.append((new_row, new_col))
            return neighbors

        for z in zeros:
            visited = set(z)
            agenda = [z]
            step = 1

            while agenda:
                current_list = agenda
                agenda = []
                for current in current_list:
                    neighbors = find_neighbors(current)
                    for n in neighbors:
                        if n not in visited:
                            agenda.append(n)
                            if grid[n[0]][n[1]] > step:
                                grid[n[0]][n[1]] = step
                        visited.add(n)
                step += 1

        return