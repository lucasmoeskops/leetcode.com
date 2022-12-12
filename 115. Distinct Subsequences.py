# Score
#  Runtime: 40%
#  Memory usage: 85%
#
# Description
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
#

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ways = defaultdict(int)
        locations = defaultdict(list)
        for index, character in enumerate(t):
            locations[character].insert(0, index)

        for character in s:
            for location in locations[character]:
                if location == 0:
                    ways[character] += 1
                else:
                    ways[t[:location+1]] += ways[t[:location]]
        
        return ways[t]
