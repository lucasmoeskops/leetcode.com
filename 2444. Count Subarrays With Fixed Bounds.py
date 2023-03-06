# Score
#  Runtime: 94%
#  Memory usage: 73%
#
# Description
# 
# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
#    The minimum value in the subarray is equal to minK.
#    The maximum value in the subarray is equal to maxK.
#
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        hasmin = hasmax = False
        total = 0
        curlength = 0
        minkat = maxkat = 0
        
        for i, c in enumerate(nums):
            curlength += 1
            
            if c == minK:
                 hasmin = True
                 minkat = i
            elif c < minK:
                 hasmin = False
                 hasmax = False
                 curlength = 0
            
            if c == maxK:
                 hasmax = True
                 maxkat = i
            elif c > maxK:
                 hasmax = False
                 hasmin = False
                 curlength = 0
            
            if hasmin and hasmax:
                 total += curlength - (i - min(maxkat, minkat))
                 
        return total
