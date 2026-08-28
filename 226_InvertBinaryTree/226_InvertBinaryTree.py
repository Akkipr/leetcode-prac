"""
Problem Link : https://leetcode.com/problems/invert-binary-tree/
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTree2(root)
        return root


    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        first_node = TreeNode(0) 
        first_node.left = root.left
        root.left = root.right
        root.right = first_node.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        
