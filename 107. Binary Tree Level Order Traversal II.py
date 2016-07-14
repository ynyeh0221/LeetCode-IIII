# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while queue:
            (root, level) = queue.pop(0)
            res[0] += [root.val]
            if root.left:
                queue += [(root.left, level+1)]
            if root.right:
                queue += [(root.right, level+1)]
            if queue and level != queue[0][1]:
                res = [[]] + res
        return res
