class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_indices(i1, i2):
            temp_list = []  # indices
            if i1 - 1 >= 0 and grid[i1-1][i2] == '1': # top element
                temp_list.append((i1-1, i2))
            if i1 + 1 < len(grid) and grid[i1+1][i2] == '1': # bottom element
                temp_list.append((i1+1, i2))
            if i2 - 1 >= 0 and grid[i1][i2-1] == '1': # left element
                temp_list.append((i1, i2-1))
            if i2 + 1 < len(grid[i1]) and grid[i1][i2+1] == '1': # right element
                temp_list.append((i1, i2+1))
            return temp_list

        visited = set()
        islands = 0
        for rowi, row in enumerate(grid):
            for coli, col in enumerate(row):
                if (rowi, coli) not in visited and col == "1":
                    agenda = [(rowi, coli)]
                    while agenda:
                        i1, i2 = agenda.pop()
                        neighbors = get_indices(i1, i2)
                        for n in neighbors:
                            if n not in visited:
                                visited.add(n)
                                agenda.append(n)
                    islands += 1
        return islands