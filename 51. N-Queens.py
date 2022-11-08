# Score:
#    Runtime: 38%
#    Memory usage: 86%

def recurse(n, remaining, taken):
    if not remaining:
        return [[]]
    row = n - len(remaining)
    out = []
    for col in remaining:
        for j, taken_col in enumerate(taken):
            if taken_col - j + i == col or col == taken_col - i + j:
                break
        else:
            s = ["." * col + "Q" + "." * (n - col - 1)]
            out.extend([s + r for r in recurse(n, [c for c in cols if c != col], taken + [col])])
    return out

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return recurse(n, [*range(n)], [])
        
