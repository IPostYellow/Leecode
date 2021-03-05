class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        if n==0:
            return False
        left=0
        right=n-1
        while(right>=left):
            mid=left+(right-left>>1)
            if nums[mid]==target:
                return True
            if nums[mid]>nums[left]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]==nums[left]:
                left+=1
            elif nums[mid]<nums[left]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False