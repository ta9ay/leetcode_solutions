# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.calcHeight(root)
            
    def calcHeight(self,node):
        if node.left is None and node.right is None:
            # print("leaf")
            return 1
        elif node.right is None:
            # print("go left")
            return 1 + self.calcHeight(node.left)
        elif node.left is None:
            # print("go right")
            return 1 + self.calcHeight(node.right)
        else:
            # print("go Down")
            # return 1+ max([self.calcHeight(node.left),self.calcHeight(node.right)])
            leftheight = self.calcHeight(node.left)
            rightheight = self.calcHeight(node.right)
            # print("left height:", leftheight)
            # print("right height:", rightheight)
            if leftheight>=rightheight:
                maxim = leftheight
            else:
                maxim = rightheight
            return 1+maxim



# OFC THERE'S A SMALLER SOLUTION
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))