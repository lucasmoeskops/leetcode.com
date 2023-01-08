# Score
#  Runtime: 79%
#  Memory usage: 82%
#
# Description
#
#  The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.
#
#  The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
#
#  Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
#
#  To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
#
#  Return the knight's minimum initial health so that he can rescue the princess.
#
#  Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
#

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        mx, my = len(dungeon[0]) - 1, len(dungeon) - 1
        health_required = [[0] * len(row) for row in dungeon]

        for y in range(len(dungeon) - 1, -1, -1):
            row = dungeon[y]

            for x in range(len(row) - 1, -1, -1):
                current = row[x]

                if x == mx and y == my:
                    from_next = 0
                else:
                    from_next = inf

                    if y < my:
                        from_next = health_required[y+1][x]
                        
                    if x < mx:
                        from_next = min(from_next, health_required[y][x+1])

                if current > 0:
                    health_required[y][x] = max(0, from_next - current)
                else:
                    health_required[y][x] = from_next - current
        
        return health_required[0][0] + 1
