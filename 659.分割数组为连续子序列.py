'''
给你一个按升序排序的整数数组 num（可能包含重复数字），
请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
 
示例 2：
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5

示例 3：
输入: [1,2,3,4,4,5]
输出: False
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import heapq
from collections import defaultdict
from typing import List


class Solution:  # 超时
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        result = [[] for i in range(len(nums) // 3)]
        count = 0
        result[0].append(nums[0])
        for i in range(1, len(nums)):
            flag = 0
            min_index = -1
            min_value = len(nums)
            for j in range(count + 1):
                if nums[i] == result[j][-1] + 1:
                    if len(result[j]) < min_value:
                        min_index = j
                        min_value = len(result[j])
                    flag = 1
            if flag == 0:
                count += 1
                if count >= len(result):
                    return False
                else:
                    result[count].append(nums[i])
            else:
                result[min_index].append(nums[i])

        for i in result:
            if i != [] and len(i) < 3:
                return False

        return True


class Solution2:  # 超时
    def isPossible(self, nums: List[int]) -> bool:
        chains = defaultdict(list)
        for i in nums:
            if not chains[i - 1]:
                heapq.heappush(chains[i], 1)
            else:
                min_len = heapq.heappop(chains[i - 1])
                heapq.heappush(chains[i], min_len + 1)
            # print(chains)
        print(chains)
        for _, chain in chains.items():
            if chain and chain[0] < 3:
                return False
        return True



# s = Solution2()
# print(s.isPossible([1, 2, 3, 3, 4, 5]))
L1 = [4, 5, 1, 6, 2, 7, 3, 8]
heapq.heapify(L1)
print(L1)
heapq.heappop(L1)
print(L1)