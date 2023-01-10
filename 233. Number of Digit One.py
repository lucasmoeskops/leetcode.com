# Score
#  Runtime: 50%
#  Memory usage: 64%
#
# Description
#
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#

class Solution:
    def countDigitOne(self, n: int) -> int:
        total = (n + 9) // 10
        x = 10
        
        while n >= x:
            total += x * (n // (10 * x)) + min(x, max(0, ((n % (x * 10)) + 1 - x)) % (x * 10))
            x *= 10
            
        return total
