# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the second half of the list
        length = 0
        cur = head
        while cur:
            length+=1
            cur=cur.next
        
        prev, cur = None, head
        for _ in range(math.ceil(length/2)):
            prev = cur
            cur = cur.next
        prev.next = None
        
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        
        first, second = head, prev
        while second:
            after_first, after_second = first.next, second.next
            first.next = second
            first = after_first
            second.next = first
            second = after_second
        


