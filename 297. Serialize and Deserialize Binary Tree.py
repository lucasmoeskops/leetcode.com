# Score
#  Runtime: 53%
#  Memory usage: 62%
#
# Description
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recurse(node):
            nonlocal data
            
            if not node:
                return
            
            data += str(node.val) + ','
            
            if node.left:
                recurse(node.left)
            else:
                data += '|'
            
            if node.right:
                recurse(node.right)
            else:
                data += '|'
        
        data = ""
        recurse(root)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
            
        root = TreeNode(-1)
        stack = [partial(setattr, root, 'left')]
        p = 0

        for i in range(len(data)):
            if data[i] == ',':
                t = TreeNode(data[p:i])
                p = i + 1
                stack.pop()(t)
                stack.append(partial(setattr, t, 'right'))
                stack.append(partial(setattr, t, 'left'))
            elif data[i] == '|':
                stack.pop()
                p += 1
                
        return root.left
