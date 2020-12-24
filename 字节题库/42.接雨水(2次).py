'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:  # 超时
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        sum = 0
        for i in range(1, len(height) - 1):
            left_max = height[i]
            right_max = height[i]
            for j in range(i - 1, -1, -1):
                left_max = max(height[j], left_max)
            for j in range(i + 1, len(height)):
                right_max = max(height[j], right_max)
            sum += min(left_max, right_max) - height[i]
        return sum


class Solution2:#56ms,13.9mb
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        sum = 0
        left_max = [height[i] for i in range(len(height))]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max=[height[i] for i in range(len(height))]
        for j in range(len(height)-2,-1,-1):
            right_max[j]=max(right_max[j+1],height[j])
        for i in range(1,len(height)-1):
            sum+=min(left_max[i],right_max[i])-height[i]
        return sum

class Solution3:#44ms,13.9mb
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        sum = 0
        left,right=0,len(height)-1
        left_max=0
        right_max=0
        while(left<right):
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            if left_max<=right_max:
                sum+=left_max-height[left]
                left+=1
            else:
                sum+=right_max-height[right]
                right-=1
        return sum

#第二次
class Solution_2:
    def trap(self, height: List[int]) -> int:

        # def find_max_height(start,height):
        #     leftm=-1
        #     rightm=-1
        #     for i in range(start):
        #         if height[i]>leftm:
        #             leftm=height[i]
        #     for i in range(start+1,len(height)):
        #         if height[i]>rightm:
        #             rightm=height[i]
        #     return leftm,rightm
        # water=0
        # for i in range(1,len(height)-1):
        #     l,r=find_max_height(i,height)
        #     if height[i]<min(l,r):
        #         water+=min(l,r)-height[i]
        # return water
        if len(height) == 0:
            return 0
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        water = 0
        while (left < right):
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax < rmax:
                water += lmax - height[left]
                left += 1
            else:
                water += rmax - height[right]
                right -= 1
        return water