"""
Problem Link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Platform     : LeetCode
Difficulty   : Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if ((root.val < p.val) and (root.val < q.val)):
            return self.lowestCommonAncestor(root.right, p, q)
            
        if ((root.val > p.val) and (root.val > q.val)):
            return self.lowestCommonAncestor(root.left, p, q)

        return root

        '''
        def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
            if root is None:
                return 0

            if ((root.val <= p.val) and (root.val <= q.val)):
                lowestCommonAncestor2(root.right, p, q)
            
            if ((root.val >= p.val) and (root.val >= q.val)):
                lowestCommonAncestor2(root.left, p, q)

            if ((root.val >= p.val) and (root.val <= q.val)):
                self.goat = root
            
            if ((root.val <= p.val) and (root.val >= q.val)):
                self.goat = root
        lowestCommonAncestor2(root, p, q)
        return self.goat
        '''
