"""
Problem Link : https://leetcode.com/problems/binary-tree-level-order-traversal/
Platform     : LeetCode
Difficulty   : Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        visited = []
        queue = deque([root])

        visited.append([root.val])
        while queue:
            size = len(queue)
            arr = []

            for _ in range(size):
                s = queue.popleft()

                if(s.left):
                    if (s.left.val not in visited):
                        arr.append(s.left.val)
                        queue.append(s.left)
                
                if(s.right):
                    if (s.right.val not in visited):
                        arr.append(s.right.val)
                        queue.append(s.right)

            if len(arr) != 0:
                visited.append(arr)
        return visited

