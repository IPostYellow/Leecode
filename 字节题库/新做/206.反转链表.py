# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p=ListNode(-1)
        t=head
        while(t!=None):
            tmp=t
            t=t.next
            tmp.next=p.next
            p.next=tmp
        return p.next
    def reverseList1(self,head):
        if head==None or head.next==None:
            return head
        else:
            res=self.reverseList1(head.next)
            head.next.next=head
            head.next=None
        return res