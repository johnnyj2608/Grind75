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
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        odd = head
        even = evenHead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head