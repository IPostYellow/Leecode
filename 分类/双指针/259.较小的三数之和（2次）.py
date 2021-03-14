"""
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
示例：
输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 和等于0的题目有异曲同工之处
        nums.sort()
        result=0
        for i in range(len(nums)-2):
            # if i >0 and nums[i]==nums[i-1]:
            #     continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]<target:
                    result=result+(r-l) # r都可以满足，说明l到r都可以满足小于target
                    # while l<r and nums[l]==nums[l+1]:
                    #     l+=1
                    # while l<r and nums[r]==nums[r-1]:
                    #     r-=1
                    l+=1
                elif nums[i]+nums[l]+nums[r]>=target:
                    r-=1
        return result

#第二次
class Solution2:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 和等于0的题目有异曲同工之处
        # 如果加一个大数都小于target，那么加他之前的小数都肯定小于target
        nums.sort()
        ans=0
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while(left<right):
                if nums[i]+nums[left]+nums[right]<target:
                    ans=ans+right-left # right之前到left的所有数都肯定加起来小于target [-2,0,1,3]
                                        #                                           [0,1,2,3]
                    left+=1 # 移动left
                else:
                    right-=1
        return ans