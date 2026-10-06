"""
Problem Link : https://leetcode.com/problems/lru-cache/
Platform     : LeetCode
Difficulty   : Medium
"""

class DoublyLinked:
    def __init__(self, val=-1, nextt=None, prev=None, key=-1):
        self.val = val
        self.next = nextt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.fake_head = DoublyLinked(-1, None, None, -1)
        self.fake_tail = DoublyLinked(-1, None, None, -1)

        self.fake_head.next = self.fake_tail
        self.fake_tail.prev = self.fake_head

        self.map = {}
        self.capacity = capacity

        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]

        if self.fake_head.next is node:
            return node.val
        else:
            left = node.prev
            right = node.next
            old_front = self.fake_head.next
            self.fake_head.next = node
            node.prev = self.fake_head
            node.next = old_front
            old_front.prev = node

            left.next = right
            right.prev = left

            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            new_node = DoublyLinked(value, None, None, key)

            #add it to the front
            current_front = self.fake_head.next
            self.fake_head.next = new_node
            new_node.prev = self.fake_head
            new_node.next = current_front
            current_front.prev = new_node

            self.map[key] = new_node

            if (len(self.map) == (self.capacity + 1)):
                # delete LRU
                delete = self.fake_tail.prev
                self.fake_tail.prev = delete.prev
                delete.prev.next = self.fake_tail

                del self.map[delete.key]
        else:
            # so node is in the map, update the value and position
            node = self.map[key]
            node.val = value

            if self.fake_head.next is node:
                return
            else:
                left = node.prev
                right = node.next
                old_front = self.fake_head.next
                self.fake_head.next = node
                node.prev = self.fake_head
                node.next = old_front
                old_front.prev = node

                left.next = right
                right.prev = left


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
