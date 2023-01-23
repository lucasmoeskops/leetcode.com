# Score
#  Runtime: 47%
#  Memory usage: 82%
#
# Description
#
#
# You are given a string s. You can convert s to a
# palindrome
# by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.
#

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
          
        half = s[:ceil(len(s) / 2)][::-1]
        
        for i in range(ceil(len(s) / 2), -1, -1):
            if half == s[i:i + i]:
                return s[2*i:][::-1] + half[::-1] + s[i:]
            
            if half[1:] == s[i:i + i - 1]:
                return s[2*i-1:][::-1] + half[::-1] + s[i:]
            
            half = half[1:]
        
        return s[::-1][:-1] + s
