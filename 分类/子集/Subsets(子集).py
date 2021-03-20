"""
给定一个不包含重复元素的数组，找出他的不重复的子集
"""


def find_subsets(nums):
    subsets = []

    def trackback(nums, start, path):
        subsets.append(path)
        for i in range(start, len(nums)):
            trackback(nums, i + 1, path + [nums[i]])

    trackback(nums, 0, [])
    return subsets


# 非递归
def findSubsets(nums):
    subsets = []
    subsets.append([])
    for cur in nums:
        n = len(subsets)  # 把当前的cur加到每一个subsets集合里
        for i in range(n):
            s=list(subsets[i])
            s.append(cur)
            subsets.append(s)
    return subsets




print(find_subsets([1, 3, 5]))
print(find_subsets([1, 5, 3]))
print(find_subsets([1, 3]))

print(findSubsets([1, 3, 5]))
print(findSubsets([1, 5, 3]))
print(findSubsets([1, 3]))