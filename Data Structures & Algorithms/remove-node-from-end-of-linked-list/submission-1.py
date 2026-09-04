# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0. Check length of list
        l = 0
        start = head
        while start:
            l += 1
            start = start.next

        if l == 1:
            return None
        
        start, end = head, head
        # 1. initialize end based on distance
        i = 0
        while i < n:
            if end is not None:
                end = end.next
            i += 1
        
        # 2. Now start and end are n elements apart
        # 2a. If end is already at None, then, you are done
        if end is None:
            return head.next

        while end.next:
            start = start.next
            end = end.next

        adj = start.next
        start.next = adj.next
        return head