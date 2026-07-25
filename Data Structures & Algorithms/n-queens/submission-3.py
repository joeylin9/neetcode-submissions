class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def create_board():
            board = []

            for _, col in queens:
                row = "." * col + "Q" + "." * (n - col - 1)
                board.append(row)

            return board

        def place_queen(coord):
            queens.append(coord)
            queen_rows.add(coord[0])
            queen_cols.add(coord[1])
            queen_diag1.add(coord[0]+coord[1])
            queen_diag2.add(coord[0]+(n-coord[1]))

        def remove_queen(coord):
            queens.pop()
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
        def helper(queen_count):
            #queens is a set of coords the queens are currently at
            if queen_count == n:
                # add board to the ans
                ans.append(create_board())
                return True
            
            #place next
            for col_i in range(n):
                coord = (queen_count, col_i)
                if check_all(coord):
                    place_queen(coord)
                    helper(queen_count+1)
                    remove_queen(coord)
            
        queens = [] #coords queens are in
        queen_rows = set()
        queen_cols = set()
        queen_diag1 = set() #bottom left to top right
        queen_diag2 = set() #top left ot bottom right
        helper(0)
        return ans



