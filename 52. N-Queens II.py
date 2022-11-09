# Score:
#    Runtime: 83%
#    Memory usage: 37%

def recurse(n, remaining, taken):
    if not remaining:
        return 1
    row = n - len(remaining)
    out = 0
    for col in remaining:
        for j, taken_col in enumerate(taken):
            if taken_col - j + i == col or col == taken_col - i + j:
                break
        else:
            out += recurse(n, [c for c in cols if c != col], taken + [col])
    return out

class Solution:
    def totalNQueens(self, n: int) -> int:
        return recurse(n, [*range(n)], [])
