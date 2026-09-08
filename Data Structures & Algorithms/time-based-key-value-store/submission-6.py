class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key]:
            return ''
        
        values = self.data[key] #list of (timestamp, values)
        l,r = 0, len(values)-1
        while l<r:
            m = (l+r+1)//2
            if values[m][0] <= timestamp:
                l=m
            else:
                r=m-1
        return values[l][1] if values[l][0] <= timestamp else ''

