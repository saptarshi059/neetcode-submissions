# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def assemble_num(ptr):
            n = []
            while ptr:
                n.append(ptr.val)
                ptr = ptr.next
            n.reverse()
            r = ""
            for i in n:
                r += str(i)
            return int(r)

        n1 = assemble_num(l1)
        n2 = assemble_num(l2)
        res = str(n1 + n2)

        head = curr = ListNode()
        for i in range(len(res)-1, -1, -1):
            curr.next = ListNode(int(res[i]))
            curr = curr.next

        return head.next