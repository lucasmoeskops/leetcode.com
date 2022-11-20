# Score:
#  Runtime: 48%
#  Memory usage: 80%
#
# Description:
# Given a string s representing a valid expression, implement a basic calculator to evaluate it,
# and return the result of the evaluation.
#

class Solution:
    def calculate(self, s: str) -> int:
        i, j = 0, len(s)
        total = 0
        operator = None
        stack = []

        while i < j:
            token = s[i]
            i += 1

            if token == '+':
                operator = '+'
                continue
            elif token == '-':
                operator = '-'
                continue
            elif token == ' ':
                continue
            elif token == '(':
                stack.append((total, operator))
                total, operator = 0, None
                continue
            elif token == ')':
                token = total
                total, operator = stack.pop()
            else:
                while i < j and '0' <= s[i] <= '9':
                    token += s[i]
                    i += 1

                token = int(token)

            if operator:
                if operator == '+':
                    total += token
                else:
                    total -= token
            else:
                total = token

        return total
        
