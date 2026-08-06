# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def height(root):
            if root == None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            joint_height = left_height + right_height
            diameter[0] = max(diameter[0], joint_height)
            return max(1 + left_height, 1 + right_height)
        height(root)
        return diameter[0]
        
            
        