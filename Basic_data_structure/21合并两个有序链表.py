'''
将两个升序链表合并为一个新的 升序 链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:#44ms,13.4MB
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        tmp = ListNode(0)
        h = tmp
        while (l1 != None and l2 != None):
            if l1.val > l2.val:
                h.next = l2
                l2 = l2.next
                h = h.next
            else:
                h.next = l1
                l1 = l1.next
                h = h.next
        if l1:
            while (l1 != None):
                h.next, l1 = l1, l1.next
                h = h.next
        if l2:
            while (l2 != None):
                h.next, l2 = l2, l2.next
                h = h.next
        return tmp.next


P1 = ListNode(1)
P2 = ListNode(2)
P3 = ListNode(4)
P1.next = P2
P2.next = P3
O1 = ListNode(1)
O2 = ListNode(3)
O3 = ListNode(4)
O1.next = O2
O2.next = O3
S = Solution()
k = S.mergeTwoLists(P1, O1)
print(k)
