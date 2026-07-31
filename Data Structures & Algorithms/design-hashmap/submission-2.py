class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.buckets = 100
        self.heads = [None] * self.buckets

    def put(self, key: int, value: int) -> None:
        hash_value = key % self.buckets
        curr = self.heads[hash_value]
        if curr is None:
            self.heads[hash_value] = ListNode(key=key, value=value)
            return
        
        while curr:
            if curr.key == key:
                curr.value = value
                return

            # Reached tail, didn't find anything
            if curr.next is None:
                break
            
            curr = curr.next
        
        curr.next = ListNode(key=key, value=value)

    def get(self, key: int) -> int:
        hash_value = key % self.buckets
        curr = self.heads[hash_value]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        hash_value = key % self.buckets
        curr = self.heads[hash_value]
        
        if curr is None:
            return
        
        if curr.key == key:
            # Removing head node
            self.heads[hash_value] = self.heads[hash_value].next
        else:
            prev = curr
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                prev = prev.next
                curr = curr.next
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)