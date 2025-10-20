# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if root == None:
                return 0
            else:
                left_height = height(root.left)
                right_height = height(root.right)
                if abs(left_height - right_height) > 1:
                    balanced[0] = False
                    return 0
            return max(1 + left_height, 1 + right_height)
        if root == None:
            return balanced[0]
        height(root)
        return balanced[0]

        