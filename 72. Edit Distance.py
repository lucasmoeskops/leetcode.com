# Score:
#  Runtime: 58%
#  Memory usage: 93%
#
# Description:
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#

def recurse(current_cost, play_room, longest, shortest, worst_case):
    if current_cost + abs(len(longest) - len(shortest)) >= worst_case:
        # Can never be the best
        return worst_case
    
    if not shortest:
        # Done
        return current_cost + len(longest)
    
    if not longest:
        # Done
        return current_cost + len(shortest)
    
    letter = shortest[0]
    
    # This is always the best option
    if longest[0] == letter:
        return recurse(current_cost, play_room, longest[1:], shortest[1:], worst_case)
    
    # This can reduce the option space for most cases
    if letter not in longest[:max(0, play_room)]:
        # replace is most likely
        worst_case = min(worst_case, recurse(current_cost + 1, play_room, longest[1:], shortest[1:], worst_case))
    
    
    # Testing deleting the character first because this resolves faster
    worst_case = min(worst_case, recurse(current_cost + 1, play_room + 1, longest, shortest[1:], worst_case))
    
    # We loop backwards, because later cases resolve faster and reduce the possibilities of the earlier cases
    i = 0
    while i < len(longest) and current_cost + i + max(0, i - play_room) < worst_case:
        i += 1
    while i > 0:
        i -= 1
        if longest[i] == letter:
            worst_case = min(worst_case, recurse(current_cost+i, play_room-i, longest[i+1:], shortest[1:], worst_case))

    # We might have already tested replacement or we might not
    worst_case = min(worst_case, recurse(current_cost + 1, play_room, longest[1:], shortest[1:], worst_case))
    return worst_case



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Make word1 always the longest
        if len(word1) < len(word2):
            t = word1
            word1 = word2
            word2 = t
            
        # Worst case is replacing all letters and removing the remaining letters
        worst_case = len(word1)
        
        play_room = len(word1) - len(word2) + 1
        return recurse(0, play_room, word1, word2, worst_case)
  
