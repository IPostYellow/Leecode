"""
给定一个可能包含重复数字的数组，找到他所有子集
"""

def find_subsets(nums):
    subsets = []

    def trackback(nums, start, path):
        subsets.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            trackback(nums, i + 1, path + [nums[i]])

    trackback(nums, 0, [])
    return subsets

print(find_subsets([1,3,3]))
print(find_subsets([1,5,3,3]))