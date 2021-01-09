class Solution:
    def findk(self, nums, l, r):
        p1, p2 = l, r + 1
        while (p1 < p2):
            p1 += 1
            while (nums[p1] < nums[l]):
                p1 += 1
            p2 -= 1
            while (nums[p2] > nums[l]):
                p2 -= 1
            if p1 < p2:
                tmp = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = tmp
        tmp = nums[l]
        nums[l] = nums[p2]
        nums[p2] = tmp
        return p2

    def quick_sort(self, nums, left, right):
        if left < right:
            j = self.findk(nums, left, right)
            self.quick_sort(nums, left, j - 1)
            self.quick_sort(nums, j + 1, right)

s=Solution()
print(s.quick_sort([-1,-1,float('inf')],0,2))