class MedianFinder:

    def __init__(self):
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.lower and not self.upper:
            heapq.heappush(self.lower, -num)
            return

        left_max = -self.lower[0] if self.lower else math.inf
        right_min = self.upper[0] if self.upper else -math.inf
        if num <= left_max:
            if len(self.lower) > len(self.upper): #left side already has one more
                left_max = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, left_max)
            heapq.heappush(self.lower, -num)
        elif num >= right_min:
            if len(self.upper) > len(self.lower): #right side already has one more
                right_min = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -right_min)
            heapq.heappush(self.upper, num)
        else:
            # between the two, add to the smaller or add in middle
            if len(self.lower) >= len(self.upper):
                heapq.heappush(self.lower, -num)
            else:
                heapq.heappush(self.upper, num)

    def findMedian(self) -> float:
        if (len(self.lower) + len(self.upper)) % 2 == 1:
            return -self.lower[0] if len(self.lower) > len(self.upper) else self.upper[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2
        