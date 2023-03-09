# Score
#  Runtime: 95%
#  Memory usage: 97%
#
# Description
#
#   A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
#
#   The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
#
#      lefti is the x coordinate of the left edge of the ith building.
#      righti is the x coordinate of the right edge of the ith building.
#      heighti is the height of the ith building.
#
#   You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
#
#   The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
#
#   Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
#

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        stack = []
        i = 0
        
        while i < len(buildings) or stack:
            if i == len(buildings) or stack and stack[-1][0] < buildings[i][0]:
                xe, h = stack.pop()
                
                while stack and stack[-1][0] <= xe:
                    stack.pop()
                    
                if stack:
                    skyline.append([xe, stack[-1][1]])
                else:
                    skyline.append([xe, 0])
            else:
                xs, xe, h = buildings[i]
                i += 1
                
                if not stack or h > stack[-1][1]:
                    if skyline and xs == skyline[-1][0]:
                        skyline[-1][1] = h
                    else:
                        skyline.append([xs, h])
                        
                while stack and h > stack[-1][1] and xe >= stack[-1][0]:
                    stack.pop()
                    
                if not stack or h > stack[-1][1] or xe > stack[-1][0]:
                    t = []
                    
                    while stack and stack[-1][1] > h:
                        t.append(stack.pop())
                        
                    stack.append([xe, h])
                    
                    while t:
                        stack.append(t.pop())
                        
        return skyline
