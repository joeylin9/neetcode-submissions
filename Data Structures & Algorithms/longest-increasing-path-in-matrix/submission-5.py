class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        cells = [
            (matrix[i][j], i, j)
            for i in range(rows)
            for j in range(cols)
        ]
        cells.sort()

        dp = [[1] * cols for _ in range(rows)]
        ans = 1

        for value, i, j in cells:
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and matrix[ni][nj] < value
                ):
                    dp[i][j] = max(
                        dp[i][j],
                        1 + dp[ni][nj]
                    )

            ans = max(ans, dp[i][j])

        return ans