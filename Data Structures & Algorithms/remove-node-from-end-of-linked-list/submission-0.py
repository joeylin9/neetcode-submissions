# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        n2 = length - n + 1

        if n2 <= 1:
            return head.next
        
        prev, cur = None, head
        while n2-1:
            prev, cur = cur, cur.next
            n2 -= 1
        # now cur is the value you want to remove
        prev.next = cur.next

        return head

