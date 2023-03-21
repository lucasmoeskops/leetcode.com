# Solution
#  Runtime: 81%
#  Memory usage: 77%
#
# Description
#
# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
#
# Return the minimum number of patches required.
#

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 1
        patches = 0

        for m in nums:
            while i <= n and m > i:
                patches += 1
                i = i + i

            i = max(m + i, i)

        while n > i:
            patches += 1
            i = i + i
        
        return patches
