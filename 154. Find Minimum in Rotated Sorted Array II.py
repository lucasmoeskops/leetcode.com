# Score
#   Runtime: 62%
#   Memory usage: 79%
#
# Description
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#
#    [4,5,6,7,0,1,4] if it was rotated 4 times.
#    [0,1,4,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        mid = h // 2

        while l < h:
            if nums[mid] > nums[0]:
                l = mid + 1
            elif h == mid:
                break
            elif nums[mid] == nums[0]:
                t = mid

                while t > 0 and nums[t] == nums[0]:
                    t -= 1
                
                if t == 0:
                    l = mid + 1
                else:
                    h = t
            else:
                h = mid

            mid = (l + h) // 2
            
        return min(nums[0], nums[mid])
