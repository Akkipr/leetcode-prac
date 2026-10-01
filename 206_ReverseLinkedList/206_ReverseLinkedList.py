"""
Problem Link : https://leetcode.com/problems/reverse-linked-list/
Platform     : LeetCode
Difficulty   : Easy
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return head

        prev = None
        current = head

        while (current != None):
            after = current.next
            current.next = prev
            prev = current
            current = after
        

        return prev


        
