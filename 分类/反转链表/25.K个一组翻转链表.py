"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse_k(pre, k):
            """ 翻转pre后的k个节点，而且最后返回的cur是下一个的pre
            pre  cur   tmp
            1  -> 2  -> 3 ->  4 ->  5 ->  6
            cur.next=cur.next.next
            pre  cur      tmp
            1  -> 2 ->4 <- 3
                    4 ->  5 ->  6
            tmp.next=pre.next
            pre.next=tmp
            pre  tmp  cur
            1 -> 3 -> 4->5->6
            """
            count = 0
            cur = pre.next
            while count < k - 1:
                tmp = cur.next
                if cur.next:
                    cur.next = cur.next.next
                tmp.next = pre.next
                pre.next = tmp
                count += 1
            return cur

        first = ListNode(-1)
        first.next = head
        pre = first
        p = first.next
        count = 1
        while p != None:
            if count == k:  # 每数到有k个节点就开始翻转，不够k个就不用翻转了
                pre = reverse_k(pre, k)
                count = 0
                p = pre
            p = p.next  # 一定要在后面，不然新的p可能就是None了，然后count还+1了，会导致误把None也当成一个节点
            count += 1
        return first.next


s = Solution()
head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
print(s.reverseKGroup(head, 2))
