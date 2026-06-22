class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time_takes(i):
            return (target-_sorted[i][0])/_sorted[i][1]
        
        _sorted = sorted(zip(position, speed), reverse = True)
        
        fleets = 0
        last_time = -math.inf
        
        for i in range(len(_sorted)):
            current_time_takes = time_takes(i)
            # print(current_time_takes)
            if current_time_takes > last_time:
                fleets += 1
                last_time = current_time_takes
        
        return fleets