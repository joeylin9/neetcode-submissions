class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 dicts tracks beginning and ends as keys, and values is the tuple (beg, end)
        # 4 cases:
        #   1. one below a beginning --> replace cur beg with new beg and update tuple to (new_beg, end)
        #   2. one above an end --> replace cur end with new end and update tuple to (beg, new_end)
        #   3. one above an end (of lower seq) AND one below a beginning (of higher seq) --> connect to a large seq:
        #       a. replace beg with the beg of the end node, and replace end with end of the beg node
        #   4. Neither --> create a new beg and end in both dicts
    
        # example of 3
        # ends = {4: (2,4), 7: (6,7)} --> ends = {7: (2,7)}
        # begs = {2: (2,4), 6: (6,7)} --> begs = {2: (2,7)}
        # new num is 5: 
        #   find adjacent end (4), check end of the adjacent beginning (6) --> track ending 7 so
        #   del ends[4] (after tracking beg of that seq (2)), 
        #   replace ends[7] with (ends[4][beginning], 7)
        #   and del begs[6]
        #   replace begs[2] val with (2, end was 7)

        nums = set(nums)
        begs = {}
        ends = {}
        longest = 0

        for n in nums:
            if n-1 in ends and n+1 in begs:
                new_beg = ends[n-1][0]
                new_end = begs[n+1][1]
                del ends[n-1]
                del begs[n+1]
                ends[new_end] = (new_beg, new_end)
                begs[new_beg] = (new_beg, new_end)
                
                new_length = new_end-new_beg+1
                if new_length > longest:
                    longest = new_length

            elif n-1 in ends:
                cur_beg = ends[n-1][0]
                new_seq = (cur_beg, n)
                ends[n] = new_seq
                begs[cur_beg] = new_seq
                del ends[n-1]

                new_length = n - ends[n][0] + 1
                if new_length > longest:
                    longest = new_length

            elif n+1 in begs:
                cur_end = begs[n+1][1]
                new_seq = (n, cur_end)
                begs[n] = new_seq
                ends[cur_end] = new_seq
                del begs[n+1]

                new_length = begs[n][1] - n + 1
                if new_length > longest:
                    longest = new_length

            else:
                begs[n] = (n,n)
                ends[n] = (n,n)
                if 1 > longest:
                    longest = 1

        return longest