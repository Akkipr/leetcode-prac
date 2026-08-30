"""
Problem Link : https://leetcode.com/problems/binary-tree-right-side-view/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        visited = []
        queue = deque([root])


        while queue:
            size = len(queue)
            currentVal = []

            for _ in range(size):
                node = queue.popleft()
                currentVal.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            visited.append(currentVal)
        
        for i in range(len(visited)):
            replacement = visited[i][-1]
            visited[i] = replacement
        return visited

        
