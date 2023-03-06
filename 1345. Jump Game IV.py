# Score
#  Runtime: 97%
#  Memory usage: 98%
#
# Description
#
# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
#    i + 1 where: i + 1 < arr.length.
#    i - 1 where: i - 1 >= 0.
#    j where: arr[i] == arr[j] and i != j.
#
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        distances = [-1] * len(arr)
        distances[0] = 0
        queue = deque([0])
        end = len(arr) - 1
        lookup = defaultdict(list)
        
        for i, num in enumerate(arr):
            lookup[num].append(i)

        while queue:
            p = queue.popleft()
            
            if p == end:
                return distances[p]
            
            d = distances[p] + 1
            
            if arr[p] in lookup:
                for p2 in lookup[arr[p]]:
                    if distances[p2] < 0:
                        distances[p2] = d
                        queue.append(p2)
                del lookup[arr[p]]

            if distances[p+1] < 0:
                distances[p+1] = d
                queue.append(p+1)
                
            if p > 0 and distances[p-1] < 0:
                distances[p-1] = d
                queue.append(p-1)
                
