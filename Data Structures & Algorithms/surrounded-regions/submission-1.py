class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def neighbors(coord):
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            ns = []

            for d in dirs:
                new = (d[0]+coord[0], d[1]+coord[1])
                if (0<=new[0]<len(board) and 0<=new[1]<len(board[0])
                    and board[new[0]][new[1]] == 'O'):
                    ns.append(new)

            return ns
        
        edges = []
        for row_i in range(len(board)):
            if board[row_i][0] == 'O':
                edges.append((row_i, 0))
            if board[row_i][len(board[0])-1] == 'O':
                edges.append((row_i, len(board[0])-1))
        for col_i in range(len(board[0])):
            if board[0][col_i] == 'O':
                edges.append((0, col_i))
            if board[len(board)-1][col_i] == 'O':
                edges.append((len(board)-1, col_i))
        
        seen = set()
        queue = edges
        while queue:
            cell = queue.pop()
            if cell not in seen:
                seen.add(cell)
                for n in neighbors(cell):
                    if n not in seen:
                        queue.append(n)
        
        for row_i, row in enumerate(board):
            for col_i, cell in enumerate(row):
                if (row_i, col_i) not in seen and cell == 'O':
                    board[row_i][col_i] = 'X'
        



