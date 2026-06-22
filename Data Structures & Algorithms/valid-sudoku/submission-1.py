class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sections = {}
        sect = 0
        for i in range(3):
            for j in range(3):
                sections[(i,j)] = sect
                sect += 1

        seen = {}
        for i in range(9):
            seen['row' + str(i)] = set()
            seen['col' + str(i)] = set()
            seen['sect' + str(i)] = set()

        for row_i, row in enumerate(board):
            for col_i, num in enumerate(row):
                if num != '.':
                    section = sections[(row_i//3, col_i//3)]
                    if num in seen['row' + str(row_i)] or num in seen['col' + str(col_i)] or num in seen['sect' + str(section)]:
                        return False
                    seen['row' + str(row_i)].add(num)
                    seen['col' + str(col_i)].add(num)
                    seen['sect' + str(section)].add(num)
        return True