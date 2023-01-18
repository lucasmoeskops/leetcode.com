# Score
#  Runtime: 53%
#  Memory usage: 10%
# 
# Description
#
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        drop = Counter()
        
        for i in range(k):
            heappush(heap, -nums[i])

        output = [-heap[0]]
        
        for i in range(k, len(nums)):
            drop[-nums[i-k]] += 1
            heappush(heap, -nums[i])
            
            while drop[heap[0]] > 0:
                drop[heappop(heap)] -= 1
            
            output.append(-heap[0])
        
        return output
