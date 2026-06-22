# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def check_len(h):
            """"Returns True if length of linked list is at least k nodes"""
            l=0
            cur = h
            while cur:
                l += 1
                cur=cur.next
                if l >= k:
                    return True
            return False
        
        def reverse_list(h, k):
            """Reverses k nodes, returns tuple of (head, tail, next_node)"""
            prev, cur = None, h
            while k:
                k -= 1
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            return (prev, h, cur)
        
        cur = head
        first = True
        prev_t = None

        while check_len(cur):
            h, t, cur = reverse_list(cur,k)

            #need to connect prev_t to cur_h
            if first:
                output = h
                first = False
                prev_t = t
            else:
                prev_t.next = h
                prev_t = t

        if prev_t and cur: #if still cur left (next ll is less than k len)
            prev_t.next = cur
            
        return output if not first else cur

        