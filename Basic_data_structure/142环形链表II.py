'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
 
进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:  # 72ms,16.9MB
    def detectCycle(self, head: ListNode) -> ListNode:
        visted = set()
        while head != None:
            if head not in visted:
                visted.add(head)
            else:
                return head
            head = head.next
        return None


p = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(34)
p4 = ListNode(56)
p.next = p2
p2.next = p3
p3.next = p4
p4.next = p2
s = Solution()
print(s.detectCycle(p).val)


class Solution2:  # 64ms,16MB
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        slow = head
        fast = head
        while fast != None:
            slow = slow.next
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
            else:
                return None
            if slow == fast:
                break
        later = head
        while slow != later:
            slow = slow.next
            later = later.next
        return later


p = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(34)
p4 = ListNode(56)
p.next = p2
p2.next = p3
p3.next = p4
p4.next = p3
s = Solution2()
print(s.detectCycle(p).val)

'''
方法一：用set将遍历过的节点存储起来，当遇到在set中存在的节点的时候，那个节点就是环的入口
方法二：递推式。设F为环外的节点数，C为环节点数。则当slow指针到了环入口时，fast指向了以环入
口开始数第h个节点。显然h=F mod C。因为fast比slow多走了F个节点。
那么继续走C-h次，fast和slow会相遇。此时快指针，从h开始走了2(C-h)个节点。即现在应
该指向2C-h。而slow指针则是指向C-h，而（2C-h）mod C=(C-h)mod C。所以相遇的点为C-h。
此时按照fast比slow走了2倍的节点的公式可以得到
2(F+C-h)=F+N(C)+C-h
F=(N-1)C+h

新建一个later指针指向head。later指针和slow指针同时以每步一个节点的速度走直到相遇。
那么later指针走了F到环的入口的时候，slow指针刚好走到了C-h+F=NC的地方，也就是环的入口。
所以slow和later相遇的地方即为环的入口
'''
