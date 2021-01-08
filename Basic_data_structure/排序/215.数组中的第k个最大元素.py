class Solution:
    def quick_sort(self, nums, left, right):
        if left>=right:
            return
        i, j = left, right
        while (i < j):
            while (i<j and nums[i] < nums[left]):
                i += 1
            while (i<j and nums[j] >= nums[left]):
                j -= 1
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        tmp = nums[j]
        nums[j] = nums[left]
        nums[left] = tmp
        self.quick_sort(nums, left, j - 1)
        self.quick_sort(nums, j + 1, right)

    def findKthLargest(self, nums, k):
        nums.append(float("inf"))
        self.quick_sort(nums, 0, len(nums) - 1)
        print(nums)


s = Solution()
print(s.findKthLargest([3, 1, 2, 5, 6, 4], 5))
