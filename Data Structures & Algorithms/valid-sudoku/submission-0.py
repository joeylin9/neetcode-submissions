class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if (board[r][c] not in cols[c]) and (board[r][c] not in rows[r]) and (board[r][c]) not in squares[(r//3,c//3)]:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
                elif board[r][c] == '.':
                    continue
                else:
                    return False
                
        return True