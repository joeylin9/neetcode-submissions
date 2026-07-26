class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp where you use (i,j) where i is index for text1, j for text2
        dp = {}
        def helper(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>=len(text1) or j>=len(text2):
                return 0
            
            # try i and move on, try j and move on
            if text1[i] == text2[j]:
                dp[(i,j)] = helper(i+1,j+1)+1
            else:
                dp[(i,j)] = max(helper(i, j+1), helper(i+1,j))
            return dp[(i,j)]
        return helper(0,0)

        # if len(text1)>len(text2):
        #     a = text1
        #     b = text2
        # else:
        #     b = text1
        #     a = text2

        # indices = defaultdict(deque)
        # for i,c in enumerate(a):
        #     indices[c].append(i)
        
        # #find greatest increasing 
        # ans = 0
        # def helper(i, cur_length, prev_i):
        #     nonlocal ans

        #     if i == len(b):
        #         ans = max(ans, cur_length)
        #         return

        #     #take or dont take
        #     if indices[b[i]] and indices[b[i]][-1] > prev_i:
        #         last_index = indices[b[i]].popleft()
        #         helper(i+1, cur_length+1, last_index)
        #         indices[b[i]].append(last_index)

        #     helper(i+1, cur_length, prev_i)

        # helper(0,0,-1)
        # return ans


