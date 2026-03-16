# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        end = head
        n = 1

        # calculate n
        while end.next:
            end = end.next
            n += 1
        
        k %= n
        if k == 0:
            return head

        # find start
        newTail = head
        for _ in range(n - k - 1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        end.next = head  # make cycle

        return newHead