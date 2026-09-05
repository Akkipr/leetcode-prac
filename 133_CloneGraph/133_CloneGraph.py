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
        if node is None:
            return 
        start = node
        stack = [start]
        dictionary = {}
        visited = set()
        visited.add(start)

        while stack:
            s = stack.pop(0)
            dictionary[s] = Node(val=s.val)

            for neighbor in s.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        for key, val in dictionary.items():
            for nei in key.neighbors:
                new_nei = dictionary[nei]
                val.neighbors.append(new_nei)
        
        return dictionary[start]









        '''
        ORIGINAL
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
        '''
        
