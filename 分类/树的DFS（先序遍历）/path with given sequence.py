"""
给定一棵二叉树和一个序列，判断是否有一条路径（从根节点到叶子节点）是和序列一样的
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    # 判断是否存在一个sequence路径
    def dfs(root, sequence, index):
        if not root:
            return False
        if index >= len(sequence) or root.val != sequence[index]:  # 如果路径中出现不等的，直接返回false，超长度也直接返回false
            return False
        if not root.left and not root.right and index == len(
                sequence) - 1:  # 前面如果root.val != sequence[index]就直接返回False了，这里可以直接认为是root.val==sequence[index],如果此时root是叶子节点并且sequence也是最后一个元素了，那么就是成功找到了路径
            return True
        return dfs(root.left, sequence, index + 1) or dfs(root.right, sequence, index + 1)  # 若没有成功找到路径，则去这个节点的子树里找

    return dfs(root, sequence, 0)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
