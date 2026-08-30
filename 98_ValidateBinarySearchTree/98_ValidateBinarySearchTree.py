"""
Problem Link : https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.num = -1
        self.true = True

        def isValidBST2(root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root is None:
                return 

            isValidBST2(root.left, root)
            print(root.val)
            if self.num != -1:
                if root.val <= self.num:
                    self.true = False
            self.num = root.val
            isValidBST2(root.right, root)
        isValidBST2(root,root)
        return self.true
