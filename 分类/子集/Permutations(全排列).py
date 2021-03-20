"""
给定一组不重复的数组，找到所有全排列
"""

import copy
def find_permutations(nums):
    result = []
    nums.sort()

    def trackback(nums, used, path):
        if len(path) == len(nums):
            result.append(path)
            return
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                trackback(nums, used, path + [nums[i]])
                used[i] = 0

    used = [0 for _ in range(len(nums))]
    trackback(nums, used, [])
    return result

def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
