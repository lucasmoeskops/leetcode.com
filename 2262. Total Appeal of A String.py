# Score
#  Runtime: 75%
#  Memory usage: 100%
#
# Description
#
# The appeal of a string is the number of distinct characters found in the string.
#
#    For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
#
# Given a string s, return the total appeal of all of its substrings.
#
# A substring is a contiguous sequence of characters within a string.
#

class Solution:
    def appealSum(self, s: str) -> int:
        totals = 0
        cursum = 0
        last_seen = defaultdict(int)
        
        for i in range(len(s)):
            cursum += i - last_seen[s[i]] + 1
            last_seen[s[i]] = i + 1
            totals += cursum
            
        return totals
