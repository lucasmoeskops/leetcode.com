# Solution
#  Runtime: 84%
#  Memory usage: 17%
#
# Description
#
#   Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
#
#   Assume a BST is defined as follows:
#
#   * The left subtree of a node contains only nodes with keys less than the node's key.
#   * The right subtree of a node contains only nodes with keys greater than the node's key.
#   * Both the left and right subtrees must also be binary search trees.
#

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if not node:
                return True, inf, -inf, 0, 0
                
            if not node.left and not node.right:
                return True, node.val, node.val, node.val, node.val
                
            left_isbin, left_minkey, left_maxkey, left_cursum, left_bestsum = recurse(node.left)
            right_isbin, right_minkey, right_maxkey, right_cursum, right_bestsum = recurse(node.right)
            
            if left_isbin and right_isbin and left_maxkey < node.val < right_minkey:
                t = left_cursum + right_cursum + node.val
                return True, min(node.val, left_minkey), max(node.val, right_maxkey), t, max(t, left_bestsum, right_bestsum)
            
            return False, inf, -inf, 0, max(left_bestsum, right_bestsum)
            
        return max(0, recurse(root)[4])
