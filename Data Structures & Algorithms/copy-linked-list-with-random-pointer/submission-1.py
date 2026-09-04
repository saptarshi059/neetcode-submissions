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
        if not head:
            return None
        
        # 1. We need to create a mapping from old nodes to the new nodes so that we can easily connect the pointers
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(x=curr.val)
            curr = curr.next

        # 2. Now, just connect the pointers between the new nodes, based on the information given by the old nodes
        curr = head
        while curr:
            old_next = curr.next
            old_random = curr.random
            new_node = old_to_new[curr]
            new_node.next = old_to_new[old_next] if old_next is not None else None
            new_node.random = old_to_new[old_random] if old_random is not None else None
            curr = curr.next
        
        return old_to_new[head]