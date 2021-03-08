# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack=[root]
        cur_level_node=len(stack)
        result=[]
        tmp_result=[]
        while(stack):
            tmp=stack.pop(0)
            tmp_result.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
            cur_level_node-=1
            if cur_level_node==0:
                result.append(tmp_result)
                cur_level_node=len(stack)
                tmp_result=[]
        for i in range(len(result)):
            if i%2==1: #反着打印
                result[i].reverse()
        return result