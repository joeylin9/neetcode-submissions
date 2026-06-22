# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        prev1, prev2 = None, None

        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            
            val_sum = val1+val2
            if carry:
                val_sum += 1
                
            if val_sum>=10:
                val_sum = val_sum % 10
                carry = 1
            else:
                carry = 0

            if cur1:
                cur1.val = val_sum
                prev1, cur1 = cur1, cur1.next
            else:
                prev1 = None
            if cur2:
                cur2.val = val_sum
                prev2, cur2 = cur2, cur2.next
            else:
                prev2 = None
        
        if prev1:
            if carry:
                prev1.next = ListNode(1)
            return l1
        if prev2:
            if carry:
                prev2.next = ListNode(1)
            return l2
            
        

