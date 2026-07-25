class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # def check_all(coord):
        #     return all([check_diagonal(coord), check_row(coord), check_col(coord)])

        # def check_diagonal(coord):
        #     #topleft
        #     cur_row, cur_col = coord
        #     while 0<=cur_row<n and 0<=cur_col<n:
        #         if (cur_row, cur_col) in queens:
        #             return False
        #         cur_row, cur_col = cur_row - 1, cur_col - 1
        #     #bottom right
        #     cur_row, cur_col = coord
        #     while 0<=cur_row<n and 0<=cur_col<n:
        #         if (cur_row, cur_col) in queens:
        #             return False
        #         cur_row, cur_col = cur_row + 1, cur_col + 1

        #     #topright
        #     cur_row, cur_col = coord
        #     while 0<=cur_row<n and 0<=cur_col<n:
        #         if (cur_row, cur_col) in queens:
        #             return False
        #         cur_row, cur_col = cur_row - 1, cur_col + 1

        #     #bottomleft
        #     cur_row, cur_col = coord
        #     while 0<=cur_row<n and 0<=cur_col<n:
        #         if (cur_row, cur_col) in queens:
        #             return False
        #         cur_row, cur_col = cur_row + 1, cur_col - 1

        #     return True

        # def check_col(coord):
        #     for row_i in range(n):
        #         if (row_i, coord[1]) in queens:
        #             return False
        #     return True

        # def check_row(coord):
        #     for col_i in range(n):
        #         if (coord[0], col_i) in queens:
        #             return False
        #     return True

        def create_board(queens):
            board = []

            for row_i in range(n):
                row = ['.'] * n
                for col_i in range(n):
                    if (row_i, col_i) in queens:
                        row[col_i] = 'Q'
                board.append(''.join(row))

            return board

        def place_queen(coord):
            queens.add(coord)
            queen_rows.add(coord[0])
            queen_cols.add(coord[1])
            queen_diag1.add(coord[0]+coord[1])
            queen_diag2.add(coord[0]+(n-coord[1]))

        def remove_queen(coord):
            queens.remove(coord)
            queen_rows.remove(coord[0])
            queen_cols.remove(coord[1])
            queen_diag1.remove(coord[0]+coord[1])
            queen_diag2.remove(coord[0]+(n-coord[1]))
        
        def check_all(coord):
            return not (coord[0] in queen_rows
                or coord[1] in queen_cols
                or coord[0]+coord[1] in queen_diag1
                or coord[0]+(n-coord[1]) in queen_diag2)

        ans = []
        def helper(queen_count, row):
            #queens is a set of coords the queens are currently at
            if queen_count == n:
                # add board to the ans
                ans.append(create_board(queens))
                return True
            
            #place next
            for col_i in range(n):
                coord = (row, col_i)
                if check_all((row, col_i)):
                    place_queen(coord)
                    helper(queen_count+1, row+1)
                    remove_queen(coord)
            
        queens = set() #set of coords queens are in
        queen_rows = set()
        queen_cols = set()
        queen_diag1 = set() #bottom left to top right
        queen_diag2 = set() #top left ot bottom right
        helper(0, 0)
        return ans



