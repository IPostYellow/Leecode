"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return root
        que=[root]
        while que:
            size=len(que)
            for i in range(size):
                tmp=que.pop(0)

                if i==size-1:
                    tmp.next=None
                else:
                    tmp.next=que[0]

                if tmp.left:
                    que.append(tmp.left)
                if tmp.right:
                    que.append(tmp.right)
        return root