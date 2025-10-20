# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            
            return isIdentical(p.left, q.left) and isIdentical(p.right, q.right)
            
        def has_subTree(root):
            if not root:
                return False
            
            if isIdentical(root, subRoot):
                return True
            
            return has_subTree(root.left) or has_subTree(root.right)
        
        return has_subTree(root)
        