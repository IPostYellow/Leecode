'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:#60ms,13.6mb
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        def jinwei(v1, v2, ad):
            if v1 + v2 + ad >= 10:
                return True
            else:
                return False

        p1 = l1
        p2 = l2
        if p1.val + p2.val < 10:
            p3 = ListNode(p1.val + p2.val)
            ad = 0
        else:
            p3 = ListNode((p1.val + p2.val) % 10)
            ad = 1
        p1 = p1.next
        p2 = p2.next
        first = p3
        while (p1 != None and p2 != None):
            if jinwei(p1.val, p2.val, ad):
                tmp = ListNode((p1.val + p2.val + ad) % 10)
                ad = 1
            else:
                tmp = ListNode(p1.val + p2.val + ad)
                ad = 0
            p3.next = tmp
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            if ad:
                if jinwei(p1.val, 0, ad):
                    tmp = ListNode((p1.val + ad) % 10)
                    ad = 1
                else:
                    tmp = ListNode(p1.val + ad)
                    ad = 0
            else:
                tmp = ListNode(p1.val)
            p3.next = tmp
            p3 = p3.next
            p1 = p1.next

        while p2:
            if ad:
                if jinwei(p2.val, 0, ad):
                    tmp = ListNode((p2.val + ad) % 10)
                    ad = 1
                else:
                    tmp = ListNode(p2.val + ad)
                    ad = 0
            else:
                tmp = ListNode(p2.val)
            p3.next = tmp
            p3 = p3.next
            p2 = p2.next
        if ad == 1:
            tmp = ListNode(1)
            p3.next = tmp

        return first