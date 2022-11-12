# Score:
#  Runtime: 62%
#  Memory usage: 12%
#
# Description:
#  Implement the MedianFinder class:
#
#   MedianFinder() initializes the MedianFinder object.
#   void addNum(int num) adds the integer num from the data stream to the data structure.
#   double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
#

def binsearch_left(array, x):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high + 1) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    mid = (low + high + 1) // 2
    return mid
    

class MedianFinder:

    def __init__(self):
        self.nums = deque()

    def addNum(self, num: int) -> None:
        loc = binsearch_left(self.nums, num)
        self.nums.insert(loc, num)

    def findMedian(self) -> float:
        half, odd = divmod(len(self.nums), 2)
        return self.nums[half] if odd else (self.nums[half-1]+self.nums[half]) / 2
