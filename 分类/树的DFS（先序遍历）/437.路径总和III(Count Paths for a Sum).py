"""
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1  # 表示自己就是一种

        def dfs(root, curSum):
            if not root:
                return 0
            curSum += root.val
            cnt = hashmap[curSum - sum]  # curSum-sum看看在路径中有没有出现过
            hashmap[curSum] += 1
            leftcnt = dfs(root.left, curSum)
            rightcnt = dfs(root.right, curSum)
            hashmap[curSum] -= 1
            curSum -= root.val
            return cnt + leftcnt + rightcnt

        """
        5
     4    8
  11     13   4
7   2        5  1
        """
        return dfs(root, 0)

"""
hashmap{0:1,5:1,9:1,20:1,27:1}
            27-22=5 说明27-5=22 说明 5到27这一段里的和为22
sum=22
5 4 11 7
"""
