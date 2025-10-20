# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNodes(node, p, q):
            if not node:
                return
            if node.val < p.val and node.val < q.val:
                return findNodes(node.right, p, q)
            elif node.val > p.val and node.val > q.val:
                return findNodes(node.left, p, q)
            elif node.val == p.val or node.val == q.val:
                return node
            return node
        return findNodes(root, p, q)
            