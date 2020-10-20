'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:#744ms，48.9mb
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        if length <= 1:
            return head
        middle=self.dived(head)
        cur=middle.next
        middle.next=None #head剩下前半个链表
        middle=cur#middle变成后一条链表
        left=self.sortList(head)
        right=self.sortList(middle)
        return self.merge(left,right)

    def dived(self, head):#找到中间结点
        if head == None or head.next == None:
            return head
        p1=head
        p2=head
        while(p2.next!=None and p2.next.next!=None):
            p1=p1.next
            p2=p2.next.next

        return p1

    def merge(self,l1,l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<l2.val:
            l1.next=self.merge(l1.next,l2)
            return l1
        else:
            l2.next=self.merge(l1,l2.next)
            return l2

class Solution2:#360ms，28.8mb
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

p1 = ListNode(4)
p2 = ListNode(2)
p3 = ListNode(1)
p4 = ListNode(3)
p1.next = p2
p2.next = p3
p3.next = p4
S = Solution()
print(S.sortList(p1).val)
