"""
Problem Link : https://leetcode.com/problems/diameter-of-binary-tree/
Platform     : LeetCode
Difficulty   : Easy
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.num = 0

        def diameterOfBinaryTree2(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_height = diameterOfBinaryTree2(root.left)
            right_height = diameterOfBinaryTree2(root.right)
            max_height = left_height + right_height
            self.num = max(self.num, max_height)
            return 1 + max(left_height,right_height)

        diameterOfBinaryTree2(root)
        return self.num
            
