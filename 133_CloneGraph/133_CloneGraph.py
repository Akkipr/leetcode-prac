"""
Problem Link : https://leetcode.com/problems/clone-graph/
Platform     : LeetCode
Difficulty   : Medium
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = []
        seen2 = []
        stack = [node]
        if not node:
            return None
        if node:
            current_node: Optional['Node'] = Node(node.val)
        else:
            current_node = None
        stack2 = [current_node]
        while stack:
            s = stack.pop(0)
            r = stack2.pop(0)
            if s not in seen:
                seen.append(s)
                seen2.append(r)

                for neighbor in s.neighbors:
                    print(neighbor.val)
                    ok: Optional['Node'] = Node(neighbor.val)
                    for i in range(len(seen)):
                        if seen[i] == neighbor:
                            ok = seen2[i]
                    for i in range(len(stack)):
                        if stack[i] == neighbor:
                            ok = stack2[i]
                    r.neighbors.append(ok)
                    stack.append(neighbor)
                    stack2.append(ok)

        return current_node
        
