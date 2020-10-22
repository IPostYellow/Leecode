'''
给定一个链表，
删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # 44ms,13.5mb
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p2 = ListNode(0)
        p2.next = head
        p1 = head
        res = p2
        for i in range(n - 1):
            p1 = p1.next
        while (p1.next != None):
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return res.next


class Soulution2:#36ms,13.6mb
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        count = n
        while (count > 0):
            if p1.next == None:
                return head.next
            p1 = p1.next
            count -= 1

        while (p1.next != None):
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return head


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

s = Solution()
# k = s.removeNthFromEnd(p1, 2)
# print(k)
# o1=ListNode(1)
# d=s.removeNthFromEnd(o1,1)
o2 = ListNode(1)
o3 = ListNode(2)
o2.next = o3
dd = s.removeNthFromEnd(o2, 2)
print(dd)
