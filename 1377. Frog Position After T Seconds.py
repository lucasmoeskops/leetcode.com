# Solution
#  Runtime: 86%
#  Memory usage: 43%
#
# Description
#
#   Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.
#
#   The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
#
#   Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.
#

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        lookup = defaultdict(list)
        
        for a, b in edges:
            lookup[a].append(b)
            lookup[b].append(a)
        
        queue = deque([(1, 0, 0, 1)])
        
        while queue and queue[0][1] <= t:
            at, when, before, prob = queue.popleft()
            
            if at == target and when == t:
                return prob
            
            children = [x for x in lookup[at] if x != before]
            
            for child in children:
                queue.append((child, when + 1, at, prob / len(children)))
            
            if at == target and not children:
                return prob

        return 0
