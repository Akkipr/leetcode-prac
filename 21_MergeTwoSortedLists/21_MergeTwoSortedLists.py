"""
Problem Link : https://leetcode.com/problems/merge-two-sorted-lists/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        start = ListNode(0)
        new_list = start

        i = 0
        while i <= 50 and (list1 is not None or list2 is not None):

            if list1 is not None:
                while list1 is not None and list1.val == i:
                    new_list.val = list1.val
                    list1 = list1.next

                    if list1 is not None or list2 is not None:
                        new_list.next = ListNode(0)
                        new_list = new_list.next

            if list2 is not None:
                while list2 is not None and list2.val == i:
                    new_list.val = list2.val
                    list2 = list2.next

                    if list1 is not None or list2 is not None:
                        new_list.next = ListNode(0)
                        new_list = new_list.next

            i += 1

        return start
