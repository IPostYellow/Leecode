class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=l+(r-l>>1)
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[0]:
                if nums[mid]>target>=nums[0]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<nums[0]:
                if nums[len(nums)-1]>=target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return -1