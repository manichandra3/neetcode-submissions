# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        def split_half(h: Optional[ListNode]):
            """Return (first_head, second_head). First gets ceil(n/2) nodes."""
            slow = fast = h
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            return h, second
        def reverse(h: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = h
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        def interlink(first: Optional[ListNode], second: Optional[ListNode]) -> None:
            """Interleave nodes from second into first in-place. Modifies lists."""
            p1, p2 = first, second
            while p2:
                n1 = p1.next
                n2 = p2.next
                p1.next = p2
                p2.next = n1
                p1 = n1
                p2 = n2
        first, second = split_half(head)
        second = reverse(second)
        interlink(first, second)
