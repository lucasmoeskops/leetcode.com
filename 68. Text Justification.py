# Score:
#  Runtime: 27%
#  Memory usage: 54%
#
# Description:
#
# Given an array of strings words and a width maxWidth, format the text
# such that each line has exactly maxWidth characters and is fully
# (left and right) justified.
#

def justify(line, length, maxWidth, is_last):
    if is_last or len(line) == 1:
        return " ".join(line) + " " * (maxWidth - length)
    num_space, space_limit = divmod(maxWidth - length, len(line) - 1)
    out = line[0]
    i = 1
    while i < len(line):
        out += " " * (num_space + 1 + (i <= space_limit))
        out += line[i]
        i += 1
    return out


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        while i < len(words):
            line = [words[i]]
            l = len(words[i])
            i += 1
            while i < len(words) and l + len(words[i]) < maxWidth:
                line.append(words[i])
                l += len(words[i]) + 1
                i += 1
            lines.append(justify(line, l, maxWidth, i >= len(words)))
        return lines
