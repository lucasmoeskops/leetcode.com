# Score
#   Runtime: 92%
#   Memory usage: 58%

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest_missing = 1
        
        for i, n in enumerate(nums, start=1):
            while 0 < n < i:
                if nums[n-1] == n:
                    break
                nums[i-1] = nums[n-1]
                nums[n-1] = n
                n = nums[i-1]
                
        for n in nums:
            if n != smallest_missing:
                return smallest_missing
                
            smallest_missing += 1
            
        return len(nums) + 1
