# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(l_idx, r_idx, previous_l, left_node):
            prev = previous_l
            curr = left_node
            for i in range(l_idx, r_idx):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
        if left == right:
            return head

        # 1. Find prev_L
        prev_l = None
        l = head
        i = 0
        while i < left-1:
            prev_l = l
            l = l.next
            i += 1
        
        # 2. Find next_r
        r = None
        next_r = head
        i = 0
        while i < right:
            r = next_r
            next_r = next_r.next
            i += 1

        # 3. Reverse between l and r
        reverse(left, right+1, prev_l, l)
        
        # 4. Adjust pointers
        if prev_l:
            prev_l.next = r
            l.next = next_r
        else:
            head = r
            l.next = next_r


        return head