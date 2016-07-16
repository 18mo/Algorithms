# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:    return False

        sum -= root.val
        if sum == 0 and self.isLeaf(root):  return True;
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def isLeaf(self, node):
        return node.left == None and node.right == None
