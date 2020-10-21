'''
给定一个链表和一个特定值 x，对链表进行分隔，
使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:#48ms,13.6mb
    def partition(self, head: ListNode, x: int) -> ListNode:
        p1 = ListNode(0)
        res = p1
        p2 = ListNode(0)
        tmp = p2
        p = head
        while (p != None):
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p2.next = None
        p1.next = tmp.next
        return res.next


p1 = ListNode(1)
p2 = ListNode(4)
p3 = ListNode(3)
p4 = ListNode(2)
p5 = ListNode(5)
p6 = ListNode(2)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
s = Solution()
k = s.partition(p1, 3)
print(s.partition(p1, 3).val)
