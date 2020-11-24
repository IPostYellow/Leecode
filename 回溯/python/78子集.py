import copy
'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import itertools

'''
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''

class Solution1:
    def subsets(self, nums):
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


class Solution2:  # 迭代
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + j for j in res]
        return res

# s = Solution2()
# print(s.subsets([1, 2, 3]))



class Solution3:

    def subsets(self, nums):
        result = []

        def backtrack(nums, start, track):
            track = copy.deepcopy(track)
            result.append(track)
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1, track)
                track.pop(-1)

        backtrack([1,2,3],0,[])
        return result

s = Solution3()
print(s.subsets([1, 2, 3]))
