class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def neighbors(coord):
            dirs = [(0,1), (0,-1), (-1, 0), (1,0)]
            neighs = []
            for d in dirs:
                new_coord = (d[0] + coord[0], d[1] + coord[1])
                if 0<=new_coord[0]<len(board) and 0<=new_coord[1]<len(board[0]):#in bounds
                    neighs.append(new_coord)
            return neighs
    
        def helper(cur_word, coord):
            if len(cur_word) >= len(word):
                if cur_word == word:
                    return True
                else:
                    return False
            
            for n in neighbors(coord):
                if n not in visited:
                    visited.add(n)
                    if helper(cur_word + board[n[0]][n[1]], n):
                        return True
                    visited.remove(n)
            return False
        
        for row_i, row in enumerate(board):
            for col_i, cell in enumerate(row):
                visited = {(row_i, col_i)}
                if helper(cell, (row_i, col_i)):
                    return True
        return False
