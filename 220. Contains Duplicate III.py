# Score
#  Runtime: 44%
#  Memory usage: 16%
#
# Description
#
# You are given an integer array nums and two integers indexDiff and valueDiff.
#
# Find a pair of indices (i, j) such that:
#
#    i != j,
#    abs(i - j) <= indexDiff.
#    abs(nums[i] - nums[j]) <= valueDiff, and
#
# Return true if such pair exists or false otherwise.
#

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff == 0:
            seen_recently = set()
            
            for i in range(len(nums)):
                if nums[i] in seen_recently:
                    return True
                
                seen_recently.add(nums[i])
                
                if i >= indexDiff:
                    seen_recently.remove(nums[i-indexDiff])
            
            return False
        
        if indexDiff == 1:
            for a, b in pairwise(nums):
                if abs(a-b) <= valueDiff:
                    return True

        nums = sorted(zip(nums, count()))
        
        for k, (a, i) in enumerate(nums):
            for (b, j) in islice(nums, k+1, None):
                if b - a > valueDiff:
                    break

                if abs(i - j) <= indexDiff:
                    return True
        
        return False
  
