# Score
#  Runtime: 100%
#  Memory usage: 20%
#
# Description
#
# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.
#
# Note that operands in the returned expressions should not contain leading zeros.
#

known_ao = {}
known_mul = {}

def check_multiplication(num, target):
    if len(num) < len(str(target)):
        return []

    if len(num) == 1:
        return [num] if int(num) == target else []

    if num[0] == '0':
        if target == 0:
            return ['0*' + option for option, amount in all_multiplication(num[1:])]
        else:
            return []
    
    options = []

    if int(num) == target:
        options.append(num)

    for i in range(1, len(num)):
        p = int(num[:i])
        if not target % p:
            for option in check_multiplication(num[i:], target // p):
                options.append(num[:i] + '*' + option)

    return options


def all_multiplication(num):
    if num in known_mul:
        return known_mul[num]

    options = [(num, int(num))] if num[0] != '0' or len(num) == 1 else []
    until = 2 if num[0] == '0' and len(num) > 1 else len(num)

    for i in range(1, until):
        p = int(num[:i])
        
        for option, amount in all_multiplication(num[i:]):
            options.append((num[:i] + '*' + option, amount * p))

    known_mul[num] = options
    return known_mul[num]


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if (num, target) in known_ao:
            return known_ao[(num, target)]
            
        if len(num) < len(str(target)):
            return []

        if len(num) == 1:
            return [num] if int(num) == target else []

        options = []
        options.extend(check_multiplication(num, target))

        for i in range(1, len(num)):
            for option, amount in all_multiplication(num[:i]):
                for option2 in self.addOperators(num[i:], target-amount):
                    options.append(option + '+' + option2)

                for option2 in self.addOperators(num[i:], amount-target):
                    options.append(option + '-' + option2.replace('-', 'X').replace('+', '-').replace('X', '+'))
        
        known_ao[(num, target)] = options
        return known_ao[(num, target)]
