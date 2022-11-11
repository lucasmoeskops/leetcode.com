# Score:
#  Runtime: 14%
#  Memory usage: 75%
#
# Description:
# Given a string s, return true if s is a valid number.
#

DIGIT_START = ord('0')
DIGIT_END = ord('9')

def isInteger(s: str) -> bool:
    if not s:
        return False
    
    at = s[0] == '+' or s[0] == '-'
    
    if at and len(s) == 1:
        return False
    
    for i in range(at, len(s)):
        if not (DIGIT_START <= ord(s[i]) <= DIGIT_END):
            return False
    
    return True
    
    
def isNumber(s: str) -> bool:
    if '.' in s:
        integer, fraction = s.split('.', maxsplit=1)
        
        if not (integer or fraction):
            return False
        
        if integer and not isInteger(integer):
            if integer == '-' or integer == '+':
                return isInteger(fraction)
            
            return False
        
        if fraction:
            if fraction[0] == '-' or fraction[0] == '+':
                return False
            
            if not isInteger(fraction):
                return False
        
        return True
    
    return isInteger(s)


class Solution:
    def isNumber(self, s: str) -> bool:
        if 'e' in s:
            expo_sign = 'e'
        elif 'E' in s:
            expo_sign = 'E'
        else:
            expo_sign = 0
            
        if expo_sign:
            number, exponent = s.split(expo_sign, maxsplit=1)
            
            if not isInteger(exponent):
                return False
        else:
            number = s
            
        return isNumber(number)
