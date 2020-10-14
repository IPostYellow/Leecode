'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:#52ms,13.6MB
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newhead=ListNode(0)
        newhead.next=head
        pre=newhead
        cur=newhead.next
        step=0
        while(step<m-1):
            pre=pre.next
            cur=cur.next
            step+=1
        for i in range(0, n - m):
            tmp = cur.next
            if cur.next:
                cur.next = cur.next.next
            tmp.next = pre.next
            pre.next = tmp
        return newhead.next

