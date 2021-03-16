"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。\
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 假设头到环起点距离为a，环内距离为b，设相遇的时候快指针走的路程为f，慢指针走的路程为s
        # 则有f=s+nb f=2s =>f=2nb s=nb #快指针比慢指针多走了n圈
        # 一个指针从头到一圈重新回环口的距离为nb+a
        # 又已知慢指针已经走了nb，只要再走a就到环入口了，此时只要从头开始再弄一个指针，也走a步就会与慢指针相遇
        if not head:
            return None
        p1=head
        p2=head
        while p2.next!=None and p2.next.next!=None:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                break
        if p2.next==None or p2.next.next==None:
            return None
        else:
            p2=head
            while p2!=p1:
                p1=p1.next
                p2=p2.next
        return p1

# 第二次
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 设fast和slow相遇的结果为2f和f
        # 则2f=f+nb ->f=nb 那易知a+nb=环入口那么只要再让slow走a就好了，和从头的起点一起走，走到相遇就是a了
        if not head or head.next==None:
            return None
        fast,slow=head,head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if fast.next==None or fast.next.next==None: #用这个判断甚至可以省去判断head.next==None
            return None
        fast=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

