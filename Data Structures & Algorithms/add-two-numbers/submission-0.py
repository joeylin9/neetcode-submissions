# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = '', ''
        cur1 = l1
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
        
        num1 = ''.join(reversed(list(num1)))
        num2 = ''.join(reversed(list(num2)))

        ans = str(int(num1) + int(num2))
        sum_head = ListNode(int(ans[-1]))
        cur=sum_head
        for i in range(len(ans)-1):
            cur.next = ListNode(int(ans[-i-2]))
            cur = cur.next
        return sum_head
        
