class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyHashSet:
    def __init__(self):
        self.max_val = 100
        self.start_ptrs = [None] * self.max_val # List of head pointers

    def add(self, key: int) -> None:
        if not self.contains(key):
            start_val = key % self.max_val
            # This means that the LL for this head does not exist
            if self.start_ptrs[start_val] is None:
                self.start_ptrs[start_val] = ListNode(key)
            else:
                # The start node exists, so traverse to find empty spot
                curr = self.start_ptrs[start_val]
                while curr.next is not None:
                    curr = curr.next
                curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            start_val = key % self.max_val            
            # Case 1: Trying to remove head node
            if self.start_ptrs[start_val].val == key:
                    self.start_ptrs[start_val] = self.start_ptrs[start_val].next
            else:
                p = self.start_ptrs[start_val]
                c = self.start_ptrs[start_val].next
                while c.val != key:
                    p = p.next
                    c = c.next
                p.next = c.next

    def contains(self, key: int) -> bool:
        start_val = key % self.max_val
        # This means the head itself does not exist
        if self.start_ptrs[start_val] is None:
            return False
        else:
            curr = self.start_ptrs[start_val]
            while curr is not None:
                if curr.val == key:
                    return True
                curr = curr.next
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)