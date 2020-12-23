'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。


示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5


说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse_from_p1_to_p2(p1,p2,prev): #翻转p1到p2的链表，最后p1指向的是最后的节点，而p2才是指向开始的节点
            end=p2.next
            t=ListNode(-1)
            t.next=end
            while(p1!=end):
                tmp=p1
                p1=p1.next
                tmp.next=t.next
                t.next=tmp
            prev.next=t.next

        first=ListNode(-1)
        first.next=head
        res=first
        p=first #末尾
        while(p.next!=None):
            count=k
            while(count!=0):
                p=p.next
                count-=1
                if p==None:
                    return res.next
            reverse_from_p1_to_p2(head,p,first)
            end=head
            head=head.next
            p=end
            first=end

        return res.next

p1=ListNode(1)
p2=ListNode(2)
p3=ListNode(3)
p4=ListNode(4)
p5=ListNode(5)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
s=Solution()
print(s.reverseKGroup(p1,2))