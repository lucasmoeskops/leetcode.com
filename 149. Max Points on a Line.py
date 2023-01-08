# Score
#  Runtime: 84%
#  Memory usage: 57%
#
# Description
#
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 1

        for i, (x1, y1) in enumerate(points[:-1]):
            from_point = Counter()

            for j, (x2, y2) in enumerate(points[i+1:], start=i+1):
                dx = x2 - x1
                dy = y2 - y1
                f = gcd(dx, dy)
                from_point[(dx // f, dy // f)] += 1
                from_point[(-dx // f, -dy // f)] += 1

            max_points = max(max_points, max(from_point.values()) + 1)

            if max_points > len(points) - max_points - i:
                break

        return max_points
