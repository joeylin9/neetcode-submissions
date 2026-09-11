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
        cur3 = ListNode()
        head3 = cur3
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur3.val = cur1.val
                cur1 = cur1.next
            else:
                cur3.val = cur2.val
                cur2 = cur2.next
            if not cur1: #cur2 may still be left
                cur3.next = cur2
                return head3
            elif not cur2:
                cur3.next = cur1
                return head3
            next_node = ListNode()
            cur3.next = next_node
            cur3 = next_node
        return head3