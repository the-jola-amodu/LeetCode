# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root, maximum, minimum):
            if not root:
                return True
            
            if root.val >= maximum or root.val <= minimum:
                return False

            result = recurse(root.left, root.val, minimum) and recurse(root.right, maximum, root.val)
            return result

        return recurse(root, float('inf'), float('-inf'))
        