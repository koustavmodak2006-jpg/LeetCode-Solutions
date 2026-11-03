# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        res = []
        ans = 0
        temp = head
        while temp:
            res.append(temp.val)
            temp = temp.next
        for i in range(len(res)//2):
            ans = max(ans, res[i] + res[-(i+1)])
        return ans