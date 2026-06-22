# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = ListNode()
        cur_dummy = cur
        
        while lists:
            smallest = None
            smallest_id = None
            for i, head in enumerate(lists):
                if not smallest or head.val < smallest.val:
                    smallest = head
                    smallest_id = i

            # found smallest head
            cur.next = smallest
            cur = cur.next
            if not smallest.next:
                lists.pop(smallest_id)
            else:
                lists[smallest_id] = smallest.next
        return cur_dummy.next

    

