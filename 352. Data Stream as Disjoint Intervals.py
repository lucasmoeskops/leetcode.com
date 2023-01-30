# Score
#  Runtime: 92%
#  Memory usage: 99%
#
# Description
#
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.
#
# Implement the SummaryRanges class:
#
#    SummaryRanges() Initializes the object with an empty stream.
#    void addNum(int value) Adds the integer value to the stream.
#    int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
#

class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.nums = {}
        self.clean = True

    def addNum(self, value: int) -> None:
        if value in self.nums:
            return
        
        if value - 1 in self.nums:
            interval = self.nums[value - 1]

            if interval[1] >= value:
                return
                
            self.nums[value] = interval
            interval[1] = value
        else:
            interval = [value, value]
            self.intervals.append(interval)
            self.clean = False
            self.nums[value] = interval

        if value + 1 in self.nums:
            old_interval = self.nums[value + 1]
            interval[1] = old_interval[1]

            for n in range(value + 1, interval[1] + 1):
                self.nums[n] = interval
                
            old_interval[0] = -1
            self.clean = False
    
    def make_clean(self):
        self.intervals = [interval for interval in self.intervals if interval[0] != -1]
        self.intervals = sorted(self.intervals)
        self.clean = True

    def getIntervals(self) -> List[List[int]]:
        if not self.clean:
            self.make_clean()
        
        return self.intervals
