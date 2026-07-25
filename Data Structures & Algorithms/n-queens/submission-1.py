class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check_all(coord):
            return all([check_diagonal(coord), check_row(coord), check_col(coord)])

        def check_diagonal(coord):
            #topleft
            cur_row, cur_col = coord
            while 0<=cur_row<n and 0<=cur_col<n:
                if (cur_row, cur_col) in queens:
                    return False
                cur_row, cur_col = cur_row - 1, cur_col - 1
            #bottom right
            cur_row, cur_col = coord
            while 0<=cur_row<n and 0<=cur_col<n:
                if (cur_row, cur_col) in queens:
                    return False
                cur_row, cur_col = cur_row + 1, cur_col + 1

            #topright
            cur_row, cur_col = coord
            while 0<=cur_row<n and 0<=cur_col<n:
                if (cur_row, cur_col) in queens:
                    return False
                cur_row, cur_col = cur_row - 1, cur_col + 1

            #bottomleft
            cur_row, cur_col = coord
            while 0<=cur_row<n and 0<=cur_col<n:
                if (cur_row, cur_col) in queens:
                    return False
                cur_row, cur_col = cur_row + 1, cur_col - 1

            return True

        def check_col(coord):
            for row_i in range(n):
                if (row_i, coord[1]) in queens:
                    return False
            return True

        def check_row(coord):
            for col_i in range(n):
                if (coord[0], col_i) in queens:
                    return False
            return True

        def create_board(queens):
            board = []

            for row_i in range(n):
                row = ['.'] * n
                for col_i in range(n):
                    if (row_i, col_i) in queens:
                        row[col_i] = 'Q'
                board.append(''.join(row))

            return board

        
        ans = []
        def helper(queen_count, queens, row):
            #queens is a set of coords the queens are currently at
            if queen_count == n:
                # add board to the ans
                ans.append(create_board(queens))
                return True
            
            #place next
            for col_i in range(n):
                if check_all((row, col_i)):
                    queens.add((row, col_i)) # place
                    # if not helper(queen_count+1, queens, row+1): #if not work
                    helper(queen_count+1, queens, row+1)
                    queens.remove((row, col_i)) #remove
            
            return False

        queens = set() #set of coords queens are in
        helper(0, queens, 0)
        return ans



