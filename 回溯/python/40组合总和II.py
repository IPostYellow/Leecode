'''
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:# 48ms,13.6mb
    def combinationSum2(self, candidates, target: int):
        nums=sorted(candidates)
        result=[]
        def trackback(start,sum,track):
            for i in range(start,len(nums)):
                if (i>start) and (nums[i]==nums[i-1]):
                    continue
                if sum+nums[i]==target:
                    result.append(track+[nums[i]])
                    return
                if sum+nums[i]>target:
                    return
                if sum+nums[i]<target:
                    trackback(i+1,sum+nums[i],track+[nums[i]])
        trackback(0,0,[])
        return result