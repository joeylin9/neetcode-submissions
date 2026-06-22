# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        cur1, cur2 = list1, list2
        if cur1.val > cur2.val:
            head = cur2
            cur = cur2
            cur2 = cur2.next
        else:
            head = cur1
            cur = cur1
            cur1 = cur1.next

        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur, cur2 = cur2, cur2.next
            else:
                cur.next = cur1
                cur, cur1 = cur1, cur1.next
        
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        
        return head

