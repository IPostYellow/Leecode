class Solution:
    def find_pos(self, nums, l, r):
        p1 = l
        p2 = r + 1
        mid=l+(r-l>>1)
        nums[l],nums[mid]=nums[mid],nums[l]
        pos = nums[p1]
        while (p1 < p2):
            p1 += 1
            while (nums[p1] < pos):
                p1 += 1
            p2 -= 1
            while (nums[p2] > pos):
                p2 -= 1
            if p1 < p2:
                tmp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = tmp
        nums[l] = nums[p2]
        nums[p2] = pos
        return p2

    def quick_sort(self, nums, left, right, k):
        if left < right:
            pos = self.find_pos(nums, left, right)
            if pos == len(nums) - k - 1:
                return nums[pos]
            if pos > len(nums) - k - 1:
                return self.quick_sort(nums, left, pos - 1, k)
            if pos < len(nums) - k - 1:
                return self.quick_sort(nums, pos + 1, right, k)
        if left == len(nums) - k - 1:
            return nums[left]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.append(float("inf"))
        res = self.quick_sort(nums, 0, len(nums) - 1, k)
        return res

# 优化一下
class Solution2:
    def find_pos(self, nums, l, r):
        p1 = l
        p2 = r + 1
        pos = nums[p1]
        while (p1 < p2):
            p1 += 1
            while (nums[p1] < pos):
                p1 += 1
            p2 -= 1
            while (nums[p2] > pos):
                p2 -= 1
            if p1 < p2:
                tmp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = tmp
        nums[l] = nums[p2]
        nums[p2] = pos
        return p2

    def quick_sort(self, nums, left, right, k):
        while left < right:
            mid = left + (right - left >> 1)
            nums[left], nums[mid] = nums[mid], nums[left]
            pos = self.find_pos(nums, left, right)
            if pos == len(nums) - k - 1:
                return nums[pos]
            if pos > len(nums) - k - 1:
                right = pos - 1
            if pos < len(nums) - k - 1:
                left = pos + 1
        if left == len(nums) - k - 1:
            return nums[left]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.append(float("inf"))
        res = self.quick_sort(nums, 0, len(nums) - 1, k)
        return res