# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd = cur = head
        even = evenHead = head.next

        i = 1
        while cur:
            if i > 2 and i % 2 != 0:
                odd.next = cur
                odd = odd.next
            elif i > 2 and i % 2 == 0:
                even.next = cur
                even = even.next
            cur = cur.next
            i += 1
        even.next = None
        odd.next = evenHead
        return head