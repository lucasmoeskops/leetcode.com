# Score:
#  Runtime: 80%
#  Memory usage: 27%
#
# Description:
#
#   You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
#
#   You are also given a string s of length n, where s[i] is the character assigned to node i.
#
#   Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.
#

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def recurse(node):
            nonlocal best
            child_tails = []
            for child in children[node]:
                if s[child] != s[node]:
                    child_tails.append(recurse(child))
                else:
                    recurse(child)
            
            vals = sorted(child_tails)[-2:]
            best = max(best, 1 + sum(vals))
            return 1 + (vals[-1] if vals else 0)

        children = defaultdict(list)
        for i, p in enumerate(parent):
            children[p].append(i)

        best = 0
        return max(recurse(0), best)
