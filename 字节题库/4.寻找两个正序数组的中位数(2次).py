'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1
和 nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 思路就是找到两个有序数组中第K小的值，避免奇偶讨论，可以找第(m+n+1)/2和第(m+n+2)/2个数，如果是奇数则两个数相等除以二是一样的
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        zhongwei1 = -1
        zhongwei2 = -1
        right1 = 0
        right2 = 0
        mid = (n + m) // 2
        while (right1 + right2 <= mid):
            zhongwei1 = zhongwei2
            if (right1 < m and (
                    right2 >= n or nums1[right1] < nums2[right2])):  # right1没有越界，并且right2已经越界或者没有越界但是nums1更小
                zhongwei2 = nums1[right1]
                right1 += 1
            elif (right2 < n and (right1 >= m or nums1[right1] >= nums2[right2])):
                zhongwei2 = nums2[right2]
                right2 += 1

        if (n + m) % 2 == 1:
            return float(zhongwei2)
        else:
            return (zhongwei1 + zhongwei2) / 2


s = Solution()
print(s.findMedianSortedArrays([], [1]))


# 二分法思路：
class Solution2:
    def findknumber(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        '''
        递归出口：
        当K=1时候，相当于求最小值，我们只要比较nums1和nums2的起始位置i和j上的数字就可以了。
        一般情况：
        取两个数组中的第k/2个元素（midVal1和midVal2）进行比较，如果midVal1 < midVal2，
        则说明数组1中的前k/2个元素不可能成为第k个元素的候选，所以将数组1中的前k/2个元素去掉，
        作为新数组和数组2求第k-k/2小的元素，因为我们把前k/2个元素去掉了，所以相应的k值也应该减少k/2。
        midVal1 > midVal2的情况亦然。
        边界问题：
        当某一个数组的起始位置大于等于其数组长度时，说明其所有数字均已经被淘汰了，
        相当于一个空数组了，那么实际上就变成了在另一个数组中找数字，直接就可以找出来了。
        由于两个数组的长度不定，所以有可能某个数组元素数不足k/2，所以我们需要先检查一下，
        数组中到底存不存在第K/2个数字，如果存在就取出来，否则就赋值上一个整型最大值，这样肯定会大于另一个数组的第k/2个元素，
        从而把另一个数组的前k/2个元素淘汰。

        '''
        midval1 = nums1[start1 + k // 2 - 1] if (start1 + k // 2 - 1) < len(nums1) else float("INF")
        midval2 = nums2[start2 + k // 2 - 1] if (start2 + k // 2 - 1) < len(nums2) else float("INF")

        if midval1 < midval2:
            return self.findknumber(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        else:
            return self.findknumber(nums1, start1, nums2, start2 + k // 2, k - k // 2)

    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findknumber(nums1, 0, nums2, 0, left) + self.findknumber(nums1, 0, nums2, 0, right)) / 2


#第二次
class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left, right = -1, -1
        s1, s2 = 0, 0
        mid = (m + n) // 2
        while (s1 + s2 <= mid):
            left = right
            if s1 < m and (s2 >= n or nums1[s1] < nums2[s2]):
                right = nums1[s1]
                s1 += 1
            elif s2 < n and (s1 >= m or nums2[s2] <= nums1[s1]):
                right = nums2[s2]
                s2 += 1

        if (m + n) % 2 == 0:
            return (left + right) / 2
        else:
            return float(right)


class Solution4:
    def findknumber(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2 + k - 1]
        if start2 >= len(nums2):
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        mid1 = nums1[start1 + k // 2 - 1] if (start1 + k // 2 - 1 < len(nums1)) else float("INF")
        mid2 = nums2[start2 + k // 2 - 1] if (start2 + k // 2 - 1 < len(nums2)) else float("INF")
        if mid1 < mid2:
            return self.findknumber(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        else:
            return self.findknumber(nums1, start1, nums2, start2 + k // 2, k - k // 2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findknumber(nums1, 0, nums2, 0, left) + self.findknumber(nums1, 0, nums2, 0, right)) / 2