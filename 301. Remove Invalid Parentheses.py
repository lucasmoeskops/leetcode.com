# Score
#  Runtime: 94%
#  Memory usage: 78%
#
# Description
#
#   Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
#
#   Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.
#

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = 0
        offset = 0

        options = {s}

        for k, c in enumerate(s):
            if c == "(":
                level += 1
            elif c == ")":
                level -= 1

            if level < 0:
                new = set()

                for option in options:
                    i = 0

                    while i <= k - offset:
                        j = i

                        if option[i] != ')':
                            i += 1
                            continue

                        while i <= k - offset and option[i] == ')':
                            i += 1

                        new.add(option[:i-1] + option[i:])
                        i += 1

                options = new
                level = 0
                offset += 1

        level = 0
        offset = 0
        
        for k, c in enumerate(reversed(s)):
            if c == ")":
                level += 1
            elif c == "(":
                level -= 1

            if level < 0:
                new = set()

                for option in options:
                    i = len(option) - 1

                    while i >= len(option) - k + offset - 1:
                        j = i

                        if option[i] != '(':
                            i -= 1
                            continue

                        while i >= len(option) - k + offset - 1 and option[i] == '(':
                            i -= 1

                        new.add(option[:i+1] + option[i+2:])
                        i -= 1

                options = new
                level = 0
                offset += 1

        return list(options)
