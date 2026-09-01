"""
Problem Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Platform     : LeetCode
Difficulty   : Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if not inorder:
            return None
        
        root = TreeNode(preorder[0])
        midpoint = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:midpoint+1], inorder[:midpoint])
        root.right = self.buildTree(preorder[midpoint+1:], inorder[midpoint+1:])
        return root

