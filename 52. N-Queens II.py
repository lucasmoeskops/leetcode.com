# Score:
#    Runtime: 83%
#    Memory usage: 37%

def recurse(n, remaining, taken):
    if not remaining:
        return 1
    row = n - len(remaining)
    out = 0
    for col in remaining:
        for taken_row, taken_col in enumerate(taken):
            if taken_col - taken_row + row == col or col == taken_col - row + taken_row:
                break
        else:
            out += recurse(n, [c for c in remaining if c != col], taken + [col])
    return out

class Solution:
    def totalNQueens(self, n: int) -> int:
        return recurse(n, [*range(n)], [])
