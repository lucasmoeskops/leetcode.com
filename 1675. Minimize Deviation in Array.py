# Score
#  Runtime: 90%
#  Memory usage: 100%
#
# Description
#
# You are given an array nums of n positive integers.
#
# You can perform two types of operations on any element of the array any number of times:
#
#    If the element is even, divide it by 2.
#        For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
#    If the element is odd, multiply it by 2.
#        For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
#
# The deviation of the array is the maximum difference between any two elements in the array.
#
# Return the minimum deviation the array can have after performing some number of operations.
#

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num % 2:
                nums[i] *= 2

        nums = sorted(nums)

        best = inf
        ulti_lowest = None
        
        while True:
            j = len(nums) - 1
            lowest = nums[0]
            highest = lowest

            while j >= 1:
                n = nums[j]

                while not n % 2 and n // 2 > lowest:
                    n //= 2

                if n % 2:
                    ulti_lowest = max(n, ulti_lowest) if ulti_lowest else n

                lowest = min(lowest, n)
                highest = max(highest, n)

                if n == nums[j]:
                    highest = max(highest, nums[j-1])
                    break

                nums[j] = n
                j -= 1

            highest = max(highest, nums[0])
            
            if highest - lowest < best:
                best = min(best, highest - lowest)
                
                if highest % 2:
                    break

                lim = (ulti_lowest + lowest if ulti_lowest else lowest * 2) / 1.5 
                nums = [n // 2 if not n % 2 and n >= lim else n for n in nums]
                nums = sorted(nums)

                if ulti_lowest is None:
                    ulti_lowest = next((x for x in reversed(nums) if x % 2), None)
            else:
                break
                
        return best
