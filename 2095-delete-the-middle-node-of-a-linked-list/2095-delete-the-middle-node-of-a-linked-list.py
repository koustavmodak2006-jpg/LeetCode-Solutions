# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None
        slow = fast = temp = head
        count = 0
        while fast and fast.next:
            if count >0:
                temp = temp.next
            fast = fast.next.next
            slow = slow.next
            count +=1
        temp.next = slow.next
        slow.next = None
        return head