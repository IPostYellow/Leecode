'''
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

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
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:#44ms,13.5MB
    def middleNode(self, head: ListNode) -> ListNode:
        p,q=head,head
        flag=1
        while(p.next!=None):
            if flag:
                q=q.next
                flag=0
            else:
                flag=1
            p=p.next
        return q

P1=ListNode(1)
P2=ListNode(2)
P3=ListNode(3)
P4=ListNode(4)
P5=ListNode(5)
P1.next=P2
P2.next=P3
P3.next=P4
P4.next=P5
S=Solution()
print(S.middleNode(P1).val)