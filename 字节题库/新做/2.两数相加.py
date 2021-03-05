# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ad=0
        p1=l1
        p2=l2
        result=ListNode(-1)
        t=result
        while(p1!=None and p2!=None):
            tmp=p1.val+p2.val+ad
            if tmp>=10:
                tmp-=10
                ad=1
            else:
                ad=0
            new_node=ListNode(tmp)
            t.next=new_node
            t=t.next
            p1=p1.next
            p2=p2.next
        while p1!=None:
            tmp=p1.val+ad
            if tmp>=10:
                tmp-=10
                ad=1
            else:
                ad=0
            new_node=ListNode(tmp)
            t.next=new_node
            t=t.next
            p1=p1.next
        while p2!=None:
            tmp=p2.val+ad
            if tmp>=10:
                tmp-=10
                ad=1
            else:
                ad=0
            new_node=ListNode(tmp)
            t.next=new_node
            t=t.next
            p2=p2.next
        if ad==1:
            t.next=ListNode(1)
        return result.next