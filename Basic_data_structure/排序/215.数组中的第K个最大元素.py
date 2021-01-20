

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

    def findKthLargest(self, nums, k):
        nums.append(float('inf'))
        n = len(nums)
        left, right = 0, n - 1
        while (left < right):
            # mid = left + (right - left) >> 1
            # # 将中间的数换到第一个去配合这个快排
            # tmp = nums[left]
            # nums[left] = nums[mid]
            # nums[mid] = tmp
            position = self.findk(nums, left, right)
            if position == n - k - 1:
                return nums[position]
            elif position > n - k - 1:
                right = position-1
            else:
                left = position + 1
        if left==n-k-1:
            return nums[left]

class Solution2:
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

    def findKthLargest(self, nums, k):
        nums.append(float('inf'))
        n = len(nums)
        left, right = 0, n - 1
        while (left < right):
            mid = left + (right - left >> 1)
            # 将中间的数换到第一个去配合这个快排
            tmp = nums[left]
            nums[left] = nums[mid]
            nums[mid] = tmp
            position = self.findk(nums, left, right)
            if position == n - k - 1:
                return nums[position]
            elif position > n - k - 1:
                right = position-1
            else:
                left = position + 1
        if left==n-k-1:
            return nums[left]

import heapq
class Solution3:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        return (heapq.nlargest(k,nums)[-1])