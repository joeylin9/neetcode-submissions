class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        i=0
        while i < len(intervals)-1:
            j = i+1
            while j <= len(intervals):
                if j == len(intervals): #current can take over all | works
                    intervals[i:j] = [intervals[i]]
                    i=j
                    break
                elif intervals[i][1] < intervals[j][0]: #works
                    intervals[i:j] = [intervals[i]]
                    i = j
                    break
                else:
                    if intervals[i][1] > intervals[j][1]: #works
                        j += 1
                    else: # in the middle
                        intervals[i:j+1] = [[intervals[i][0], max(intervals[i][1], intervals[j][1])]]
                        break
        return intervals

