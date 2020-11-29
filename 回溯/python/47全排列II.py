'''
给定一个可包含重复数字的序列 nums ，
按任意顺序 返回所有不重复的全排列。
示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
提示：
1 <= nums.length <= 8
-10 <= nums[i] <= 10
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:#96ms,14mb
    def permuteUnique(self, nums):
        nums = sorted(nums)
        result = []
        used = [0 for i in nums]

        def trackback(track, used):
            if len(track) == len(nums):
                result.append(track)
                return
            for i in range(len(nums)):
                if (i > 0) and (used[i - 1] == 1) and (nums[i] == nums[i - 1]):
                    continue
                if used[i] == 0:
                    used[i] = 1
                    trackback(track + [nums[i]], used)
                    used[i] = 0
                else:
                    continue

        trackback([], used)
        return result