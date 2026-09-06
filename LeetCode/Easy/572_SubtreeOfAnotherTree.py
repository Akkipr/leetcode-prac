"""
Problem Link : https://leetcode.com/problems/subtree-of-another-tree/
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
    initial = -1
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            if root.val == subRoot.val:
                self.initial=self.func(root,subRoot)
            
            if self.initial == True:
                return self.initial
            else:
                left = self.isSubtree(root.left,subRoot)
                right = self.isSubtree(root.right,subRoot)
                return left or right
        return False
    
    def func(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        if root is not None and subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        
        print(root.val)
        
        return self.func(root.left,subRoot.left) and self.func(root.right,subRoot.right)

        
