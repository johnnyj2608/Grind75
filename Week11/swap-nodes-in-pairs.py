# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            nextPair = cur.next.next
            second = cur.next
            second.next = cur
            cur.next = nextPair
            prev.next = second
            prev = cur
            cur = nextPair
        return dummy.next