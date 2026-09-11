class ListNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        # Remove node from the list
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node):
        # Always insert at right for most recent
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            new_node = ListNode(key, value)
            self._insert(new_node)
            self.cache[key] = new_node
        else:
            if len(self.cache) < self.capacity:
                new_node = ListNode(key, value)
                self._insert(new_node)
                self.cache[key] = new_node
            else:
                new_node = ListNode(key, value)
                lru = self.left.next
                self._remove(lru)
                self.cache.pop(lru.key)
                self._insert(new_node)
                self.cache[key] = new_node