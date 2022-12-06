# Score
#  Runtime: 75%
#  Memory usage: 6%
#
# Description
#   Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Gather horizontal increments
        horizontal = []
        for y, row in enumerate(matrix):
            line = []
            i = 0
            for x, val in enumerate(row):
                if val == "1":
                    i += 1
                else:
                    i = 0
                line.append(i)
            horizontal.append(line)

        # Gather vertical increments
        vertical = []
        for val in matrix[0]:
            vertical.append([int(val == "1")])
        for row in matrix[1:]:
            for x, val in enumerate(row):
                if val == "1":
                    vertical[x].append(vertical[x][-1] + 1)
                else:
                    vertical[x].append(0)

        # Walk points of interest and find their size
        best = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                max_width = horizontal[y][x]
                max_height = vertical[x][y]
                if max_width * max_height > best:
                    width = height = 1
                    while height < max_height and max_width * max_height > best:
                        new = horizontal[y-height][x]
                        if new * (height + 1) < max_width * height:
                            best = max(best, max_width * height)
                        max_width = min(max_width, new)
                        height += 1
                    while width < max_width and max_width * max_height > best:
                        new = vertical[x-width][y]
                        if new * (width + 1) < max_height * width:
                            best = max(best, width * max_height)
                        max_height = min(max_height, new)
                        width += 1
                    best = max(best, max_width * max_height)
        return best
