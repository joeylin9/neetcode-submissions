# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # keep head
        # traverse through list until reaching half point (one node past new_tail)
        # reverse til end, then stop at current tail
        # build new ordered list
        if not head.next or not head.next.next:
            return

        def reverse_list(h):
            """reverses a linked list and returns the new head of the linked list"""
            prev, cur = h, h.next
            h.next = None

            while cur:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            
            # prev is head of new reversed list
            return prev
        
        cur = head
        counter = 0
        while cur:
            counter += 1
            cur = cur.next
        
        node_counter = math.ceil(counter / 2) - 1
        cur = head
        while node_counter:
            cur = cur.next
            node_counter -= 1
        temp, cur.next = cur.next, None
        
        second_half = reverse_list(temp)
        cur1, cur2 = head, second_half
        while cur1 and cur2:
            temp1 = cur1.next
            cur1.next = cur2
            cur1 = temp1

            temp2 = cur2.next
            cur2.next = cur1
            cur2 = temp2
        


