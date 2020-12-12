'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:  # 3548ms,13.8mb
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


s = Solution()
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))

'''
很具小巧思。新建数组 tmp，用于保存最长上升子序列。
对原序列进行遍历，将每位元素二分插入 tmp 中。
如果 tmp 中元素都比它小，将它插到最后
否则，用它覆盖掉比它大的元素中最小的那个。
总之，思想就是让 tmp 中存储比较小的元素。这样，tmp 未必是真实的最长上升子序列，但长度是对的。
作者：coldme-2
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution2:  # 60ms,13.7mb
    def lengthOfLIS(self, nums: List[int]) -> int:
        tmp = [nums[0]]
        for i in nums[1:]:
            if i > tmp[-1]:
                tmp.append(i)
            else:
                left, right = 0, len(tmp) - 1
                while (left < right):
                    mid = left + (right - left >> 1)
                    if i > tmp[mid]:
                        left = mid + 1
                    elif i < tmp[mid]:
                        right = mid
                    else:
                        left = mid
                        break
                tmp[left] = i
        return len(tmp)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution3:  # 只通过了15个例子
    def lengthOfLIS(self, nums: List[int]) -> int:
        first = TreeNode(nums[0])
        p1 = first
        tmp = [p1]
        for i in range(1, len(nums)):
            for j in range(len(tmp)):
                if nums[i] > tmp[j].val:
                    tmp[j].right = TreeNode(nums[i])
                    tmp[j] = tmp[j].right
                else:
                    tmp[j].left = TreeNode(nums[i])
                    p2 = tmp[j].left
                    tmp.append(p2)

        def finddeepth(root):
            if root == None:
                return 0
            r = finddeepth(root.right) + 1
            return r

        p=[first]
        maxd=0
        while(p!=[]):
            tnode=p.pop()
            l=finddeepth(tnode)
            if l>maxd:
                maxd=l
            if tnode.left:
                p.append(tnode.left)
            if tnode.right:
                p.append(tnode.right)
        return maxd