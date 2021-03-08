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

def quick_sort(self, nums, left, right):
    if left < right:
        pos = self.find_pos(nums, left, right)
        self.quick_sort(nums, left, pos - 1)
        self.quick_sort(nums, pos + 1, right)