class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        water = [0 for _ in range(len(height))]
        
        r = len(height)-1
        max_height = 0
        while r >= 0:
            if height[r] >= max_height:
                max_height = height[r]
            else:
                water[r] = max_height - height[r]
            r-=1
        
        l = 0
        max_height = 0
        while l < len(height):
            if height[l] >= max_height:
                max_height = height[l]
                water[l] = min(0, water[l])
            else:
                water[l] = min(max_height - height[l], water[l])
            l+=1

        return sum(water)
                

