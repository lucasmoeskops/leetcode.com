# Score
#  Runtime: 77%
#  Memory usage: 46%
#
#
# Description
#
#   You are given a positive integer k. You are also given:
#
#   a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
#   a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
#
#   The two arrays contain integers from 1 to k.
#
#   You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.
#
#   The matrix should also satisfy the following conditions:
#
#   The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
#   The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
#
#   Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
#


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def find_resolution(items):
            has_no_dependencies = set(range(1, k+1))
            is_dependency_for = defaultdict(set)
            dependencies = defaultdict(set)
            
            for a, b in items:
                is_dependency_for[a].add(b)
                dependencies[b].add(a)
                has_no_dependencies.discard(b)
            
            resolution = []
            queue = deque([*has_no_dependencies])
            
            while queue:
                a = queue.popleft()
                resolution.append(a)
                
                for b in is_dependency_for[a]:
                    dependencies[b].discard(a)
                    
                    if not dependencies[b]:
                        queue.append(b)
            
            if len(resolution) < k:
                return []
            
            return resolution
            
        row_resolution = find_resolution(rowConditions)
        
        if not row_resolution:
            return []
            
        col_resolution = find_resolution(colConditions)
        
        if not col_resolution:
            return []
            
        matrix = [[0] * k for _ in range(k)]
        
        for i in range(k):
            matrix[i][col_resolution.index(row_resolution[i])] = row_resolution[i]
            
        return matrix
