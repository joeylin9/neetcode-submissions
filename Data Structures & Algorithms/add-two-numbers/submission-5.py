# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            res = cur1.val + cur2.val + carry
            if res >= 10:
                carry = 1
            else:
                carry = 0
            cur1.val, cur2.val = res%10, res%10
            prev = cur1
            cur1, cur2 = cur1.next, cur2.next
        if cur1: #still cur1 left
            prev = None
            while cur1:
                res = cur1.val + carry
                if res >= 10:
                    carry = 1
                else:
                    carry = 0
                cur1.val = res%10
                prev, cur1 = cur1, cur1.next
            if carry:
                prev.next = ListNode(1)
            return l1

        elif cur2:
            prev = None
            while cur2:
                res = cur2.val + carry
                if res >= 10:
                    carry = 1
                else:
                    carry = 0
                cur2.val = res%10
                prev, cur2 = cur2, cur2.next
            if carry:
                prev.next = ListNode(1)
            return l2
        
        else:
            if carry:
                prev.next = ListNode(1)
            return l1