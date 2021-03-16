"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast,slow=head,head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        if fast.next!=None:
            return slow.next
        else:
            return slow

#第二次
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        # 快指针走两步，慢指针走一步，这样就能在快指针走完的时候慢指针到达中间了
        # 值得注意的是，快指针最后有没有走完完整的两步是一个需要判断的边界条件
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast.next == None:
            return slow
        else:  # 如果fast指针后面是None说明fast最后一步没走完，这里slow需要再向前走一步
            return slow.next