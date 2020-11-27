'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import copy
from typing import List


class Solution:  # 44ms,13.8MB
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def backtrack(nums, tmp):
            if not nums:  # 结束条件。也就是得到n个数字以后
                result.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
            # 每次取去掉那个i的数，然后将其数拼起来，tmp就是已经拼好的

        backtrack(nums, [])
        return result


s = Solution()
print(s.permute([1, 2, 3]))


class Solution2:  # 44ms,13.8MB
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result = []
        used = []
        for i in nums:
            used.append(False)

        def backtrack(nums, used, tmp):
            if len(nums) == len(tmp):
                result.append(copy.deepcopy(tmp))
                return
            for i in range(len(nums)):
                if (used[i]) or (i > 0 and used[i - 1]==False and nums[i] == nums[i - 1]):
                    print("used[i]",i,used[i],"used[i-1]",used[i-1],"tmp",tmp)
                    continue
                tmp.append(nums[i])
                used[i] = True
                backtrack(nums, used, tmp)
                used[i] = False
                tmp.pop(-1)
            # 每次取去掉那个i的数，然后将其数拼起来，tmp就是已经拼好的

        backtrack(nums, used, [])
        return result


s = Solution2()
print(s.permute([1, 1, 2]))

# import copy
# class Solution3:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         self.result=[]
#         used=[]
#         for j in nums:
#             used.append(False)
#
#         self.trackback(nums,used,[])
#         return self.result
#     def trackback(self,nums,used,tmp):
#         if len(nums)==len(tmp):
#             self.result.append(copy.deepcopy(tmp))
#             return
#         for i in range(len(nums)):
#             if (used[i]):
#                 continue
#             if(i>0  and used[i]==used[i-1] and used[i-1]==False):
#                 continue
#             used[i]=True
#             self.trackback(nums,used,tmp+[nums[i]])
#             used[i]=False



class Solution4:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0
