# Score
#  Runtime: 85%
#  Memory usage: 88%
#
# Description:
# Given an array of integers heights representing the histogram's bar height where
# the width of each bar is 1, return the area of the largest rectangle in the histogram.
#

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_yet = 0
        history = {}
        last_height = 0
        
        for i in range(len(heights)):
            height = heights[i]
            
            # Only add to history if its new and has potential
            if height not in history and (len(heights) - i) * height > largest_yet:
                history[height] = i
                
            # Only check history if height is smaller than before
            if height >= last_height:
                last_height = height
                continue
                
            # Check history and delete items that are no longer valid
            for height_, at in list(history.items()):
                if height_ <= height:
                    continue
                    
                if at < history.get(height, len(heights)):
                    history[height] = at
                    
                # Record the size
                largest_yet = max(height_ * (i - at), largest_yet)
                del history[height_]
                    
        # Check remaining items for possible largest
        for height_, at in list(history.items()):
            largest_yet = max(height_ * (i - at + 1), largest_yet)
            
        return largest_yet
