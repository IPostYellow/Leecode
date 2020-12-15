'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        p = ListNode(-1)
        res = p
        while (p1 != None and p2 != None):
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return res.next


l1 = ListNode(5)
l1.next = ListNode(6)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(4)
l4.next = ListNode(7)
l2.next = l3
l3.next = l4
s = Solution()
print(s.mergeTwoLists(l2, l1))


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#第二次
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution3:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = ListNode(-1)
        res = first
        while (l1 != None and l2 != None):
            if l1.val < l2.val:
                first.next = l1
                first = first.next
                l1 = l1.next
            else:
                first.next = l2
                first = first.next
                l2 = l2.next
        if l1:
            first.next = l1
        if l2:
            first.next = l2

        return res.next

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution4:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2