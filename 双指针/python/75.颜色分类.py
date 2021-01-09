from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # p=0
        # for i in range(n):
        #     if nums[i]==0:
        #         nums[i],nums[p]=nums[p],nums[i]
        #         p+=1
        # for i in range(p,n):
        #     if nums[i]==1:
        #         nums[i],nums[p]=nums[p],nums[i]
        #         p+=1
        p1, p2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 += 1
            elif nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                if p1 < p2:  # 说明有p2的元素在p1的位置被换了，要换到p2这边
                    nums[p2], nums[i] = nums[i], nums[p2]
                p1 += 1
                p2 += 1
