"""
Problem Link : https://leetcode.com/problems/add-two-numbers/
Platform     : LeetCode
Difficulty   : Medium
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1:
            return None
        
        if not l2:
            return None
        
        new_list = ListNode(0)
        current = new_list

        l = l1
        r = l2
        carry = 0
        while True:
            if l and r:
                total = l.val + r.val + carry
                append = total % 10
                carry = total // 10
                current.next = ListNode(append)
                current = current.next
                l=l.next
                r=r.next
            elif l and not r:
                total = l.val + carry
                append = total % 10
                carry = total // 10
                current.next = ListNode(append)
                current = current.next
                l=l.next
            elif r and not l:
                total = r.val + carry
                append = total % 10
                carry = total // 10
                current.next = ListNode(append)
                current = current.next
                r=r.next
            else:
                break
        if carry:
            current.next = ListNode(1)
            current = current.next
        return new_list.next

        
