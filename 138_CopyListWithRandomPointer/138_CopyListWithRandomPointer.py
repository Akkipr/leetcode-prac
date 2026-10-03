"""
Problem Link : https://leetcode.com/problems/copy-list-with-random-pointer/
Platform     : LeetCode
Difficulty   : Medium
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        cur = head
        dictionary = {None:None}
        while cur:
            dictionary[cur] = Node(cur.val)
            cur=cur.next
                
        cur = head
        while cur:
            copy = dictionary[cur]
            copy.next = dictionary[cur.next]
            copy.random = dictionary[cur.random]
            cur=cur.next
        
        return dictionary[head]

