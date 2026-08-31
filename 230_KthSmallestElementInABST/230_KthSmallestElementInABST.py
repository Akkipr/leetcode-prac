"""
Problem Link : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        num = 1

        if root is None:
            return None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            if num == k:
                return current.val
            num += 1
            current = current.right

        '''
        self.k = k
        self.res = None
        
        def inorder(node):
            if not node or self.res is not None:
                return
            
            inorder(node.left)
            
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
                
            inorder(node.right)
            
        inorder(root)
        return self.res
        '''
        
