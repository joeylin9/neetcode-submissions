class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        water = []
        l = 0
        cur_height = 0

        while l < len(height):
            if height[l] >= cur_height:
                water.append(0)
                cur_height = height[l]
            else:
                water.append(cur_height)
            l+=1
        
        r = len(height)-1
        max_height = 0
        while r >= 0:
            if height[r] >= max_height:
                max_height = height[r]
                water[r] = 0
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
                

