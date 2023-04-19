# Solution
#  Runtime: 20%
#  Memory usage: 6%
#
# Description
#
#  You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.
#
#  However, there are city restrictions on the heights of the new buildings:
#
#     The height of each building must be a non-negative integer.
#     The height of the first building must be 0.
#     The height difference between any two adjacent buildings cannot exceed 1.
#
#  Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.
#
#  It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.
#
#  Return the maximum possible height of the tallest building.
#

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        normalized = {1: 0, n: n-1}
        
        for x, y in restrictions:
            normalized[x] = min(normalized.get(x, inf), y, x - 1)
        
        restrictions = sorted(map(list, normalized.items()))
        
        for i in range(1, len(restrictions)):
            x1, y1 = restrictions[i-1]
            x2, y2 = restrictions[i]
            restrictions[i][1] = min(y2, y1 + x2 - x1)
        
        for i in range(len(restrictions)-2, -1, -1):
            x1, y1 = restrictions[i]
            x2, y2 = restrictions[i+1]
            restrictions[i][1] = min(y1, y2 + x2 - x1)
        
        tallest = 0
        current_y = 0
        
        for (x1, y1), (x2, y2) in pairwise(restrictions):
            y2 = min(current_y + x2 - x1, y2)
            tallest = max(tallest, (x2 + y2 - x1 + current_y) // 2)
            current_y = min(y2, current_y + x2 - x1)
        
        return tallest
