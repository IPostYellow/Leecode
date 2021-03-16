"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1=head
        p2=head
        while p2.next!=None and p2.next.next!=None: #判断快指针就好了，如果没环肯定是快指针到结尾
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False

#第二次
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow,fast=head,head
        while fast.next!=None and fast.next.next!=None: #若果没有环，则终究快指针会先一步到达终点
            slow=slow.next
            fast=fast.next.next
            if slow==fast: #有环直接返回有环
                return True
        return False