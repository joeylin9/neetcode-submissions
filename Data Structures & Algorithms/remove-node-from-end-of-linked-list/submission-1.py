# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        prev, cur = None, head
        for _ in range(length-n):
            prev = cur
            cur = cur.next
        if prev:
            next_node = cur.next
            prev.next = next_node
            return head
        else: # remove the first node
            return head.next


