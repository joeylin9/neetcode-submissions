class TimeMap:

    def __init__(self):
        self.tracker = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tracker[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        target = self.tracker[key] # list of tup of (val, time)
        l,r = 0, len(target)-1
        counter = 0
        best_val = ""
        while l<=r:
            counter += 1
            mid = (l+r)//2
            prev_time = target[mid][1]
            val = target[mid][0]
            if prev_time == timestamp:
                return val
            elif prev_time > timestamp: #too big go down
                r = mid-1
            elif prev_time < timestamp: #small enough, but need to check higher
                best_val = val
                l = mid+1
        return best_val


