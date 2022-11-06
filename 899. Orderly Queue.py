# Score
#   Runtime: 90%
#   Memory usage: 74%

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        return min(s[i:]+s[:i] for i in range(len(s)))
        
