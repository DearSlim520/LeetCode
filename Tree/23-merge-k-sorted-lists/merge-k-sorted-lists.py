import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # initialize
        dummy = ListNode(0)
        p = dummy
        hq = []
        
        # put heads into the queue
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(hq, (head.val, i, head))

        while hq:
            value, index, node = heapq.heappop(hq)
            p.next = node
            if node.next:
                heapq.heappush(hq, (node.next.val, index, node.next))
            p = p.next
        
        return dummy.next
