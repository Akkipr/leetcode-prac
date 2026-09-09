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

        def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if tree1 is None or tree2 is None:
                return tree1 is tree2

            return (tree1.val == tree2.val and
                   is_same_tree(tree1.left, tree2.left) and
                   is_same_tree(tree1.right, tree2.right))

        if root is None:
            return False

        return (is_same_tree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        '''
        if root and subRoot:
            if root.val == subRoot.val:
                if self.func(root,subRoot) == True:
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
                
        return self.func(root.left,subRoot.left) and self.func(root.right,subRoot.right)
        '''
        
