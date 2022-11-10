# Score:
#    Runtime: 38%
#    Memory usage: 86%

def recurse(n, remaining, taken):
    if not remaining:
        return [[]]
    row = n - len(remaining)
    out = []
    for col in remaining:
        for taken_row, taken_col in enumerate(taken):
            if taken_col - taken_row + row == col or col == taken_col - row + taken_row:
                break
        else:
            s = ["." * col + "Q" + "." * (n - col - 1)]
            out.extend([s + r for r in recurse(n, [c for c in remaining if c != col], taken + [col])])
    return out

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return recurse(n, [*range(n)], [])
        
