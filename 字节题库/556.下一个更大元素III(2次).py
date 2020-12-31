class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:  # 找到第一个前面的小于后面的下标
                index = i - 1
                break
        if index == -1:  # 若没有则说明整个数单调递减，不会有答案
            return -1
        else:
            min_max = -1
            for i in range(len(nums) - 1, index, -1):  # 再找到那个下标后面大于它的值中的最小值
                if nums[i] > nums[index] and (min_max == -1 or nums[i] < nums[min_max]):
                    min_max = i
            tmp = nums[index]
            nums[index] = nums[min_max]
            nums[min_max] = tmp
            nums = nums[:index + 1] + sorted(nums[index + 1:])
            res = int(''.join(nums))
            if res <= 1 << 31:  # 越界判断
                return res
            else:
                return -1


# 第二次
class Solution_2:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index == -1:
            return -1
        min_index = -1
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index] and (min_index == -1 or nums[min_index] > nums[i]):
                min_index = i
        tmp = nums[index]
        nums[index] = nums[min_index]
        nums[min_index] = tmp
        newnums = nums[:index + 1] + sorted(nums[index + 1:])

        if int(''.join(newnums)) < (1 << 31):
            return int(''.join(newnums))
        else:
            return -1
