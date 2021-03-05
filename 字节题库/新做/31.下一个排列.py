from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=len(nums)-2
        while(index>=0 and nums[index]>=nums[index+1]):
            index-=1
        if index>=0:
            index2=len(nums)-1
            while(index2>index and nums[index]>=nums[index2]):
                index2-=1
            print(index2)
            print(index)
            nums[index],nums[index2]=nums[index2],nums[index]
            l=index+1
            r=len(nums)-1
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
            print(nums)
        else:
            nums.reverse()
s=Solution()
nums=[1,3,2]
s.nextPermutation([1,3,2])
print(nums)
# print(s.nextPermutation([1,3,2]))