class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        i=0
        ans = []
        while i < len(intervals)-1:
            j = i+1
            while j <= len(intervals):
                if j == len(intervals): #current can take over all | works
                    ans.append(intervals[i])
                    i=j
                    break
                elif intervals[i][1] < intervals[j][0]: #works
                    ans.append(intervals[i])
                    i = j
                    break
                else:
                    if intervals[i][1] > intervals[j][1]: #works
                        j += 1
                    else: # in the middle
                        intervals[j] = [intervals[i][0], max(intervals[i][1], intervals[j][1])]
                        i = j
                        break
            if i == len(intervals)-1:
                ans.append(intervals[i])
        return ans

