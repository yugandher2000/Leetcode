# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode()
        anchor = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                anchor.next = l1
                l1 = l1.next
            else:
                anchor.next = l2
                l2 = l2.next
            anchor = anchor.next
        anchor.next = l1 if l1 else l2
        return dummy.next
