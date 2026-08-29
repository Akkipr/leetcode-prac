"""
Problem Link : https://leetcode.com/problems/balanced-binary-tree/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.num = 0
        if root is None:
            return True

        def isBalanced2(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_height = isBalanced2(root.left) 
            right_height = isBalanced2(root.right) 
            change = abs(left_height-right_height)
            if change > 1:
                self.num=1
            return 1 + max(left_height,right_height)
        isBalanced2(root)
        if self.num !=0:
            return False
        return True
