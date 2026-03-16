# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev:
            # find each end
            end = prev
            for _ in range(k):
                if end.next is None:
                    return dummy.next
                end = end.next

            # reverse current k
            start = prev.next
            after = end.next
            end.next = None

            self.reverse(start, end)
            
            prev.next = end
            start.next = after

            # continue
            prev = start

        return dummy.next

    def reverse(self, start: ListNode, end: ListNode):
        pre, cur = None, start
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return