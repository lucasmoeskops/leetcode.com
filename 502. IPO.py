# Score
#  Runtime: 78%
#  Memory usage: 99%
#
# Description
#
# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
#
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def find():
            low = possible_until
            high = len(profits) - 1
            
            while low < high:
                mid = (low + high) // 2

                if capital[order[mid]] > w:
                    high = mid - 1
                elif capital[order[low + 1]] <= w:
                    low = mid + 1
                else:
                    break
            
            r = (low + high) // 2
            return r + 1 if capital[order[r]] <= w else r

        order = sorted(range(len(profits)), key=lambda i: capital[i])
        possible_until = 0
        heap = []

        for i in range(min(len(profits), k)):
            possible = find()

            for j in range(possible_until, possible):
                heappush(heap, -profits[order[j]])

            if not heap:
                break

            best = -heappop(heap)
            w += best
            possible_until = possible
        
        return w
