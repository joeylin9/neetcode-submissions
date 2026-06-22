class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for x,y in points:
            d = math.sqrt(x**2+y**2)
            heapq.heappush(distances, [-d,x,y])
            while len(distances)>k:
                heapq.heappop(distances)
        ans = []
        while distances:
            point = heapq.heappop(distances)
            ans.append([point[1], point[2]])
        return ans
        