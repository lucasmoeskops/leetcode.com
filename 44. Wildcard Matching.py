# Score
#   Runtime: 86%
#   Memory usage: 83%

def rec(s, p):
    """ Simplify s and p and see if we can resolve it. """
    # Do easy checks
    while p and s:
        if p[0] == '?' or p[0] == s[0]:
            p = p[1:]
            s = s[1:]
        elif p[-1] == '?' or p[-1] == s[-1]:
            p = p[:-1]
            s = s[:-1]
        elif p[0] != '*' or p[-1] != '*':
            return False
        else:
            break
    if p == '*':
        return True
    if not s or not p:
        return not s and not p
    if p[0] != '*':
        return False
    
    # (Optional) Advanced check to eliminate trivial patterns of format *[*x]** where x is the same character
    if p[-1] == '*' and len(set(p)) == 2:
        c = p.replace('*', '')[0]
        if c == '?':
            return len(s.replace('*', '')) >= p.count(c)
        return s.count(c) >= p.count(c)
    
    # Divide the pattern into sub patterns
    return divide(s, p)


def divide(s, p):
    """ Break the pattern in subpatterns based on the largest non variable length string. """
    
    # Find the largest pattern
    largest_pattern_length = 0
    largest_pattern_at = 0
    i = 0
    while i < len(p):
        if p[i] != '*':
            j = i + 1
            while j < len(p):
                if p[j] == '*':
                    break
                j += 1
            if j - i > largest_pattern_length:
                largest_pattern_length = j - i
                largest_pattern_at = i
            i = j + 1
        else:
            i += 1
    
    # For each match of the largest pattern try to resolve the subpatterns on both it's sides.
    p_ = p[largest_pattern_at:]
    for i in range(len(s) - largest_pattern_length + 1):
        s_ = s[i:]
        j = 0
        while j < largest_pattern_length and (s_[j] == p_[j] or p_[j] == '?'):
            j += 1
        if j == largest_pattern_length:
            if rec(s[:i], p[:largest_pattern_at]) and rec(s_[j:], p_[j:]):
                return True
    
    # No subpatterns matched
    return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Simple optimisation: remove double asterisks
        i = len(p) - 2
        while i >= 0:
            if p[i] == '*' and p[i + 1] == '*':
                p = p[:i+1] + p[i + 2:]
            i -= 1
            
        # Divide into smaller patterns
        return divide(s, p)
