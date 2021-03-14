"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

提示 1：
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：
输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：
输入：nums = [0,0,0]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right=0,0
        max_len=0
        zero_num=0 #保存0的个数，要保证0的个数不超过1
        while right<len(nums):
            if nums[right]==0:
                zero_num+=1
            while (zero_num>1):
                if nums[left]==0:
                    zero_num-=1
                left+=1
            max_len=max(max_len,right-left)
            right+=1
        return max_len

# 第二次
class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        zero_num = 0 #记录0的个数
        max_len = 0
        while (right < len(nums)):
            if nums[right] == 0:
                zero_num += 1

            while zero_num > 1: #保证0的个数不超过1
                if nums[left] == 0:
                    zero_num -= 1
                left += 1

            max_len = max(max_len, right - left) #因为是要删除掉一个元素的，所以不需要+1
            right += 1
        return max_len