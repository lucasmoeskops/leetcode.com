# Score:
#  Runtime: 76%
#  Memory usage: 78%


def recurse(n, k, remaining):
    if n == 0:
        return ""
    i = k * n // factorial(n)
    return str(remaining[i]) + recurse(n-1, k % factorial(n-1), remaining[:i]+remaining[i+1:])


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return rec(n, k-1, [*range(1, n+1)])
