# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, first, end, k):
        """
        将以first结点开头的k个节点翻转
        """
        new_node = ListNode(-1)  # 指向开头
        new_node.next = end.next
        tmp1 = first
        while (k > 0):
            tmp = tmp1.next
            tmp1.next = new_node.next
            new_node.next = tmp1
            tmp1 = tmp
            k = k - 1

        return new_node.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        p = head
        count = 1
        cur_head = head
        result = ListNode(-1)
        flag = 1
        while (p != None):
            if count == k:
                if flag == 1:
                    flag = 0
                    result.next = self.reverse(cur_head, p, k)
                    prev_end = cur_head
                    p, cur_head = cur_head.next, cur_head.next
                    count = 1
                else:
                    prev_end.next = self.reverse(cur_head, p, k)
                    prev_end = cur_head
                    p, cur_head = cur_head.next, cur_head.next
                    count = 1
            if p == None:
                break
            p = p.next
            count += 1

        return result.next