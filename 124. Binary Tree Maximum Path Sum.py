# Score
#  Runtime: 98%
#  Memory usage: 32%
#
# Description
#
#  A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
#  in the sequence has an edge connecting them. A node can only appear in the sequence
#  at most once. Note that the path does not need to pass through the root.
#
#  The path sum of a path is the sum of the node's values in the path.
#
#  Given the root of a binary tree, return the maximum path sum of any non-empty path.
#

def recurse(node):
    left = right = None
    
    if node.left:
        best_left, left = recurse(node.left)
    
    if node.right:
        best_right, right = recurse(node.right)
    
    if node.left and node.right:
        return (
          max(node.val, best_left, best_right, node.val + left + right, node.val + left, node.val + right),
          max(node.val + left, node.val + right, node.val)
        )
    
    if node.left:
        return (
          max(node.val, best_left, node.val + left),
          max(node.val, node.val + left)
        )
    
    if node.right:
        return (
          max(node.val, best_right, node.val + right),
          max(node.val, node.val + right)
        )
    
    return node.val, node.val

    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return recurse(root)[0]
