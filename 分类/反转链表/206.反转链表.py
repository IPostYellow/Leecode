"""
反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归方式
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)  # 假设head.next到尾部已经是反转了的，那么head.next.next就应该指向head
        head.next.next = head
        head.next = None  # 然后还要把head后面置空
        return new_head

# 迭代方式
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        # 头插法反转链表
        res=ListNode(-1)
        p=head
        while p!=None:
            tmp=p
            p=p.next
            tmp.next=res.next
            res.next=tmp
        return res.next