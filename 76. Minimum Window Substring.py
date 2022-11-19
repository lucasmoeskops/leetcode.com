# Score
#  Runtime: 84%
#  Memory usage: 37%
#
# Description:
# Given two strings s and t of lengths m and n respectively, return the 
# minimum window substring of s such that every character in t (including
# duplicates) is included in the window. If there is no such substring, 
# return the empty string "".
#

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        bank = Counter(t)
        
        best = 2**31-1
        best_at = None
        
        start = 0
        end = 0
        d = s[start]
        settled = False
        
        while end < len(s):
            c = s[end]
            end += 1
            
            if c not in t:
                if end == start + 1 and end < len(s):
                    start += 1
                    d = s[start]
                continue
                    
            bank[c] -= 1

            if not settled and bank[c] == 0 and all(v <= 0 for v in bank.values()):
                settled = True

            if c == d:
                while bank[d] < 0:
                    bank[d] += 1
                    start += 1
                    d = s[start]

                    while d not in t:
                        start += 1
                        d = s[start]

            if settled and end - start < best:
                best = end - start
                best_at = start
        
        return s[best_at:best_at+best] if best_at is not None else ""
        
