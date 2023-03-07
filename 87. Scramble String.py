# Score
#  Runtime: 31%
#  Memory usage: 29%
#
# Description
#
# We can scramble a string s to get a string t using the following algorithm:
#
#    If the length of the string is 1, stop.
#    If the length of the string is > 1, do the following:
#        Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
#        Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
#        Apply step 1 recursively on each of the two substrings x and y.
#
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
#

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def recurse(_s1, _s2):
            if len(_s1) == 1:
                return _s1 == _s2
                
            if (_s1, _s2) in lookup:
                return lookup[(_s1, _s2)]
                
            first_character = _s1[0]
            last_character = _s1[-1]
            
            fc_locations = [i for i, c in enumerate(_s2) if c == first_character]
            lc_locations = [i for i, c in enumerate(_s2) if c == last_character]
            
            tested = set()
            
            for i in fc_locations:
                for j in lc_locations:
                    r = j < i
                    
                    for k in range(min(i, j)+1, max(i, j)+1):
                        if (k, r) not in tested:
                            tested.add((k,r))
                            if r and recurse(_s1[:-k], _s2[k:]) and recurse(_s1[-k:], _s2[:k]):
                                lookup[(_s1, _s2)] = True
                                return True
                            if not r and recurse(_s1[:k], _s2[:k]) and recurse(_s1[k:], _s2[k:]):
                                lookup[(_s1, _s2)] = True
                                return True
                                
            lookup[(_s1, _s2)] = False
            return False
            
        lookup = {}
        return recurse(s1, s2)
