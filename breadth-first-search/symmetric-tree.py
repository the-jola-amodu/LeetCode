# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(p, q):
            if p == None and q == None:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            return symmetric(p.left, q.right) and symmetric(p.right, q.left)
        
        return symmetric(root.left, root.right)
        