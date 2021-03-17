"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead  # 前一个指针
        cur = newhead.next  # 后一个指针
        step = 1
        while step < m:  # 遍历到m的位置
            pre = pre.next
            cur = cur.next
            step += 1
        for i in range(n - m):  # 接下来有n-m次遍历
            tmp = cur.next  # 每次把cur.next提到pre的后面，以pre为节点进行头插法,cur其实就是尾节点，保持cur为尾节点，每次将cur.next头插进来
            if cur.next:  # 除非空值，不然每次cur指针跳过cur.next指向cur.next.next好进行下一次的遍历
                cur.next = cur.next.next
            tmp.next = pre.next  # 头插法
            pre.next = tmp  # 头插法
        """
        pre cur tmp
        1  ->2  ->3  ->4  ->5 -> 6
        |
        pre cur   tmp 
        1 ->2->4  <-3
               4->5->6
        tmp.next=pre.next
        pre.next=tmp
        pre  tmp  cur 
         1 -> 3->  2 ->4->5->6
        """
        return newhead.next
