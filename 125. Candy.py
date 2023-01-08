# Score
#  Runtime: 60%
#  Memory usage: 42%
#
# Description
#   There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
#   You are giving candies to these children subjected to the following requirements:
#
#      Each child must have at least one candy.
#      Children with a higher rating get more candies than their neighbors.
#
#   Return the minimum number of candies you need to have to distribute the candies to the children.
#

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        num = 1
        
        for i, r in enumerate(ratings[1:], start=1):
            if ratings[i] > ratings[i-1]:
                num += 1
            else:
                num = 1
            candies[i] = num

        change = True

        while change:
            change = False

            for i in range(len(ratings)):
                if i < len(ratings) - 1:
                    j = i

                    while j < len(ratings) - 1 and candies[j+1] >= candies[j] and ratings[j+1] < ratings[j]:
                        j += 1
                        
                    if j != i:
                        change = True
                        base = candies[j]
                        
                        for k in range(j - 1, i - 1, -1):
                            candies[k] = base + j - k
                            
        return sum(candies)
