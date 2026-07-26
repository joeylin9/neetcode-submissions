class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m-1,n-2):1, (m-2,n-1):1, (m-1, n-1): 1}

        def helper(coord):
            nonlocal m,n

            if coord in dp:
                return dp[coord]
            
            neighbors = []
            if coord[0]+1 < m:
                neighbors.append((coord[0]+1, coord[1]))
            if coord[1] + 1 < n:
                neighbors.append((coord[0], coord[1]+1))

            paths = 0
            for nei in neighbors:
                paths += helper(nei)

            dp[coord] = paths
            return dp[coord]

        return helper((0,0))
        