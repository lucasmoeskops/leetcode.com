#  Score
#    Runtime: 86%
#    Memory usage: 82%

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height) - 1
        trapped_height = 0
        height_left, height_right = height[left], height[right]
        
        while left <= right:
            if min(height_left, height_right) > trapped_height:
                # water at h level and below is already trapped
                total += (min(height_left, height_right) - trapped_height) * (right - left + 1)
                trapped_height = min(height_left, height_right)
            if height_left > height_right:
                right -= 1
                if right >= 0:
                    height_right = height[right]
            else:
                left += 1
                if left < len(height):
                    height_left = height[left]
                    
        # black squares are not trapping rain water
        total -= sum(min(trapped_height, y) for y in height)
        
        return total
