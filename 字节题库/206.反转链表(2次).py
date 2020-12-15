'''
反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        first = ListNode(-1)
        first.next = head
        head = head.next
        first.next.next=None
        while (head != None):
            tmp = head
            head = head.next
            tmp.next = first.next
            first.next = tmp
        return first.next

l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
def dayinlianbiao(s):
    while(s!=None):
        print(s.val)
        s=s.next
# s=Solution()
# d=s.reverseList(l1)
# dayinlianbiao(d)

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        first = ListNode(-1)
        def headinsert(first,head):
            if head==None:
                return
            else:
                tmp=head
                head=head.next
                tmp.next=first.next
                first.next=tmp
                headinsert(first,head)
            return
        headinsert(first,head)
        return first.next

s=Solution2()
dayinlianbiao(s.reverseList(l1))

#第二次
class ListNode3:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution3:#递归
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        else:
            res=self.reverseList(head.next)
            head.next.next=head
            head.next=None

            return res


class ListNode4:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution4:
    def reverseList(self, head: ListNode) -> ListNode:
        first = ListNode(-1)
        p1 = head
        while (p1 != None):
            tmp = p1
            p1 = p1.next
            tmp.next = first.next
            first.next = tmp

        return first.next