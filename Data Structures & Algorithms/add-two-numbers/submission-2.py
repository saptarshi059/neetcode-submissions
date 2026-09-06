# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s >= 10:
                # This means there is a carry
                carry = s // 10
                s = s % 10
            else:
                carry = 0

            curr.next = ListNode(s)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None and carry != 0:
            curr.next = ListNode(carry)
        elif l1 is None and l2 is None and carry == 0:
            curr.next = None
        else:
            rem_list = l1 if l1 is not None else l2
            
            while rem_list:
                s = rem_list.val + carry
                if s >= 10:
                    # This means there is a carry
                    s = s % 10
                    c = s / 10
                else:
                    carry = 0
                
                curr.next = ListNode(s)
                curr = curr.next
                rem_list = rem_list.next
            
            if carry != 0:
                curr.next = ListNode(carry)

        return head.next