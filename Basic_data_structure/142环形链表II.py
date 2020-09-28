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
