class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs while keeping array of hit path, if ends in both ocean, add to ans
        # sources are the entire edge
        # if hits another edge, can put that edge in seen
        def neighbors(coord):
            """returns neighbors that are less than or equal to in height"""
            dirs = [(0,1), (0,-1), (-1,0), (1,0)]
            ns = []
            for d in dirs:
                new = (d[0]+coord[0], d[1]+coord[1])
                if (0<=new[0]<len(heights) and 0<=new[1]<len(heights[0])
                    and heights[new[0]][new[1]] >= heights[coord[0]][coord[1]]
                ):
                    ns.append(new)
            return ns

        pac_edges = []
        atl_edges = []
        for col_i in range(len(heights[0])):
            pac_edges.append((0, col_i))
            atl_edges.append((len(heights)-1, col_i))
        for row_i in range(len(heights)):
            pac_edges.append((row_i, 0))
            atl_edges.append((row_i, len(heights[0])-1))
    
        def dfs(cur=tuple, ocean=str, seen=set):
            if cur not in seen:
                seen.add(cur)
                for n in neighbors(cur):
                    dfs(n, ocean, seen)

        pac_seen, atl_seen = set(), set()
        for edge in pac_edges:
            dfs(edge, 'pacific', pac_seen)
        for edge in atl_edges:
            dfs(edge, 'atlantic', atl_seen)
        ans = pac_seen.intersection(atl_seen)
        return [[coord[0],coord[1]] for coord in ans]

        # my_ans = [[2,4],[1,2],[0,4],[0,0],[1,1],[2,0],[1,4],[0,2],[2,2],[1,0],[1,3]]
        # true = [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
        # print('In my answer but shouldnt be')
        # for l in my_ans:
        #     if l not in true:
        #         print(l)
        # print()
        # print('Not in my ans but should be')
        # for l in true:
        #     if l not in my_ans:
        #         print(l)


        