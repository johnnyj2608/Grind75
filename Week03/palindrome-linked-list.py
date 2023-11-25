# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverse(slow)
        left = head
        right = slow
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head):
        prev = None
        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev