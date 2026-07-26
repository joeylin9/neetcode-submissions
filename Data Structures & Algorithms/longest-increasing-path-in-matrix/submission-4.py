class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # for each cell, run it
        # make a dp of every cell of its largest increasing path
        # make a visited got each run
        sys.setrecursionlimit(100000)

        def neighbors(coord):
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            ns = []
            for d in dirs:
                i,j = coord[0]+d[0], coord[1]+d[1]
                if 0<=i<len(matrix) and 0<=j<len(matrix[0]):
                    ns.append((i,j))
            return ns

        dp = {} #starting from i,j largest path
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            queue = []
            for n in neighbors((i,j)):
                if matrix[n[0]][n[1]] > matrix[i][j]:
                    queue.append(n)
            if not queue:
                dp[(i,j)] = 1
                return 1
            
            dp[(i,j)] = 0
            for n in queue:
                dp[(i,j)] = max(dp[(i,j)], 1+dfs(n[0], n[1]))
            return dp[(i,j)]
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i,j))

        return ans

