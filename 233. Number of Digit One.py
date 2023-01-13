# Score
#  Runtime: 61%
#  Memory usage: 98%
#
# Description
#
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#

class Solution:
    def countDigitOne(self, n: int) -> int:
        total = (n + 9) // 10
        x = 10
        x2 = 100

        while n >= x:
            total += x * (n // x2) + min(x, max(0, ((n % x2) + 1 - x)) % x2)
            x = x2
            x2 *= 10

        return total
