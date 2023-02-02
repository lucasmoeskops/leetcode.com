# Score:
#  Runtime: 78%
#  Memory usage: 55%
#
# Description:
#
# Given a string s, partition s such that every
# substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#

class Solution:
    def minCut(self, s: str) -> int:
        def inner(s):
            if len(s) < 2:
                return 0
              
            if s in lookup:
                return lookup[s]
              
            rev = s[::-1]

            if s == rev:
                return 0
              
            l = len(s)
            options = []
            
            for i in range(l, 0, -1):
                if s[:i] == rev[-i:]:
                    options.append(1 + inner(s[i:]))
                    
            lookup[s] = min(options)
            return lookup[s]
          
        lookup = {}
        return inner(s)
